from yattag import Doc
from scratch import Project, Sprite, Comment


def from_sprite(sprite: Sprite, doc, tag, text):
	for comment in sprite.comments.values():
		with tag('p'):
			text(comment.text)


def from_project(proj: Project):
	doc, tag, text = Doc().tagtext()
	for sprite in proj.sprites.values():
		from_sprite(sprite, doc, tag, text)
	return doc.getvalue()
