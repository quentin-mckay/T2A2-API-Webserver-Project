from main import db

project_tag = db.Table(
    'project_tag',
	db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
)