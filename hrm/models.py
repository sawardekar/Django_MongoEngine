from mongoengine import Document, EmbeddedDocument, fields


class Designation(EmbeddedDocument):
    name = fields.StringField(required=True)


class Employee(Document):
    name = fields.StringField(required=True)
    username = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    emp_id = fields.IntField()
    designation = fields.EmbeddedDocumentField(Designation)


class Department(Document):
    name = fields.StringField(required=True)



