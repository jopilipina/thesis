import kindred
import argparse
import os

if __name__ == '__main__':
	parser = argparse.ArgumentParser('Annotate a set of sentences and output the annotation')
	# parser.add_argument('--corpus', required=True, type=str, help='Plain text file containing the text to annotate')
	# parser.add_argument('--wordlists', required=True, type=str, help='Comma-delimited list of wordlists to load. Will use the basename as the entity name.')
	parser.add_argument('--outDir', required=True, type=str, help='Output directory to save annotations to')

	args = parser.parse_args()

	print("Setting up output directory")
	annotatedDir = os.path.join(args.outDir,'annotated_relations')
	if not os.path.isdir(annotatedDir):
		os.makedirs(annotatedDir)
	unannotatedDir = os.path.join(args.outDir,'missing_relations')
	if not os.path.isdir(unannotatedDir):
		os.makedirs(unannotatedDir)

	print("Loading and parsing corpus:")
	corpus = kindred.pubtator.load([30848500,30843663,30842342,30773559,30643969,30542790,30538558,30344734,30320899,30249899,
	30143034,30066882,30045295,29956783,29940632,29731995,29545845,29328462,29246119,29237428,30668358,28796247,
	29516630,28404875,29851970,28644424,27572663,17235726,28987383,30668360,29156797,28432456,30668408,30668391,
	30666790,30685130,30486290,30660651,30662662,28714960,24998847,25340791,25754026,26171037,26796853,10845553,
	30425532,30443189,30468498,30697812,30635434,30791942,30021836,30375484,28507441,29066508,29172290,29566943,
	30014643,30078020,30178167,30385371,30410866,30745738,30047193,30156405,30215037,30334403,30452490,30464681,
	30700828,30712155,30773851,30808718,30810286,30814494,30815801,30816447,30816464,30819158,30825015,30825132,
	30832661,30834050,30834052,30841910,30841426,30850021,28745322,28912139,28396580,28662516,28832075,24126199,
	27708247,27614750,28269748,28716024,27072261,28404957])
	parser = kindred.Parser()
	parser.parse(corpus)

	print("Splitting the corpus into sentences so that we can save any annotated sentences and don't need to annotate it all")
	sentenceCorpus = corpus.splitIntoSentences()

	print("Loading wordlists:")
	wordlistDict = {}
	for wordlist in args.wordlists.split(','):
		assert os.path.isfile(wordlist), 'Unable to access file: %s' % wordlist
		entityType = os.path.splitext(os.path.basename(wordlist))[0]
		wordlistDict[entityType] = wordlist
		print("  %s - %s" % (entityType,wordlist))

	assert len(wordlistDict) == 2, "This annotation tool currently only handles two entity relations of different types"

	wordlistLookup = kindred.EntityRecognizer.loadWordlists(wordlistDict, idColumn=0, termsColumn=0)

	print("Annotating entities in corpus with wordlists")
	entityRecognizer = kindred.EntityRecognizer(wordlistLookup)
	entityRecognizer.annotate(sentenceCorpus)

	print("Finding all candidate relations")
	acceptedEntityTypes = wordlistDict
	candidateBuilder = kindred.CandidateBuilder(entityCount=len(wordlistDict),acceptedEntityTypes = [tuple(sorted(wordlistDict.keys()))])
	candidateRelations = candidateBuilder.build(sentenceCorpus)

	print("Time to through some of the candidate relations and annotate some...")
	annotatedCorpus,unannotatedCorpus = kindred.manuallyAnnotate(sentenceCorpus,candidateRelations)

	print("\nSaving annotated corpus of %d sentences (with relations that you have just annotated)" % len(annotatedCorpus.documents))
	kindred.save(annotatedCorpus,'standoff',annotatedDir)

	print("Saving unannotated corpus of %d sentences (which you did not review)" % len(unannotatedCorpus.documents))
	kindred.save(unannotatedCorpus,'standoff',unannotatedDir)

# trainCorpus = kindred.bionlpst.load('2016-BB3-event-train')
# devCorpus = kindred.bionlpst.load('2016-BB3-event-dev')

# predictionCorpus = devCorpus.clone()
# predictionCorpus.removeRelations()

# classifier = kindred.RelationClassifier()
# classifier.train(trainCorpus)
# classifier.predict(predictionCorpus)

# f1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score')

# for i in predictionCorpus.getRelations():
#   print(i)