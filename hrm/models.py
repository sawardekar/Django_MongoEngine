from mongoengine import Document, EmbeddedDocument, fields


class Designation(EmbeddedDocument):
    name = fields.StringField(required=True, max_length=250)

    def __str__(self):
        return self.name


class Employee(Document):
    name = fields.StringField(required=True, max_length=250)
    username = fields.StringField(max_length=250)
    email = fields.EmailField()
    emp_id = fields.IntField()
    designation = fields.EmbeddedDocumentField(Designation)

    def __str__(self):
        return self.name

    # meta = {
    #     'abstract': True
    # }


class Department(Document):
    name = fields.StringField(required=True, max_length=250)

    def __str__(self):
        return self.name

    # meta = {
    #     'abstract': True
    # }
