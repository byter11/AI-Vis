import base64, io, os, urllib, uuid
from matplotlib import animation

def anim_to_bytes(anim):
	filename = f'{uuid.uuid4()}.gif'
	# writer = animation.FFMpegWriter(fps=5)
	print('in')
	anim.save(filename, writer='pillow')
	buf = io.BytesIO()
	with open(filename, 'rb') as f:
		buf.write(f.read())
	
	os.remove(filename)

	buf.seek(0)
	bufstr = base64.b64encode(buf.read())
	uri = urllib.parse.quote(bufstr)
	return uri