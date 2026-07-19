import socket, json

def bexec(payload, host="localhost", port=9876, timeout=60):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)); s.settimeout(timeout)
    s.sendall(json.dumps(payload).encode("utf-8"))
    buf = b""
    while True:
        try:
            chunk = s.recv(4096)
            if not chunk: break
            buf += chunk
            try: json.loads(buf.decode("utf-8")); break
            except json.JSONDecodeError: continue
        except socket.timeout: break
    s.close()
    return json.loads(buf.decode("utf-8"))

FRAME = r'''
import bpy
# find a 3D view
area = next(a for a in bpy.context.screen.areas if a.type=='VIEW_3D')
region = next(r for r in area.regions if r.type=='WINDOW')
with bpy.context.temp_override(area=area, region=region):
    bpy.ops.object.select_all(action='DESELECT')
    face = bpy.data.objects['Face']
    face.select_set(True)
    bpy.context.view_layer.objects.active = face
    bpy.ops.view3d.view_axis(type='TOP')   # +Z toward viewer, +Y up  -> face-on
    bpy.ops.view3d.view_selected()
# also print Face bbox in world coords
import mathutils
face = bpy.data.objects['Face']
cs = [face.matrix_world @ mathutils.Vector(c) for c in face.bound_box]
xs=[c.x for c in cs]; ys=[c.y for c in cs]; zs=[c.z for c in cs]
print("FACE bbox X:%.2f..%.2f Y:%.2f..%.2f Z:%.2f..%.2f" % (min(xs),max(xs),min(ys),max(ys),min(zs),max(zs)))
'''
print(bexec({"type":"execute_code","params":{"code":FRAME}}))
shot = bexec({"type":"get_viewport_screenshot","params":{"filepath": r"D:\blender_mcp_assets\head_shot.png", "max_size": 1000, "format":"png"}})
print(shot)
