class Relationships:
  def __init__(self, gene, disease, relation, text):
    self.gene = gene
    self.disease = disease
    self.relation = relation
    self.text = text

  def __repr__(self):
    return "Relationship('{}', '{}', '{}', '{}')".format(self.gene, self.disease, self.relation, self.text)
