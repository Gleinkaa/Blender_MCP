import socket, json, sys

def blender_exec(code, host="localhost", port=9876, timeout=60):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.settimeout(timeout)
    payload = json.dumps({"type": "execute_code", "params": {"code": code}})
    s.sendall(payload.encode("utf-8"))
    buf = b""
    while True:
        try:
            chunk = s.recv(4096)
            if not chunk:
                break
            buf += chunk
            try:
                json.loads(buf.decode("utf-8"))
                break
            except json.JSONDecodeError:
                continue
        except socket.timeout:
            break
    s.close()
    return json.loads(buf.decode("utf-8"))

CODE = r'''
import bpy

fbx = r"D:\blender_mcp_assets\chicken\WhiteChicken_anim.fbx"

# Only import if not already present
have_arm = any(o.type == 'ARMATURE' for o in bpy.data.objects)
if not have_arm:
    bpy.ops.import_scene.fbx(filepath=fbx)

print("=== OBJECTS ===")
for o in bpy.data.objects:
    print(f"{o.type:10} | {o.name:30} | verts={len(o.data.vertices) if o.type=='MESH' else '-'}")

print("\n=== ARMATURES / BONES ===")
for o in bpy.data.objects:
    if o.type == 'ARMATURE':
        print(f"ARMATURE: {o.name}  (matrix_world loc={tuple(round(v,3) for v in o.matrix_world.translation)})")
        for b in o.data.bones:
            hx,hy,hz = b.head_local
            tx,ty,tz = b.tail_local
            par = b.parent.name if b.parent else "-"
            print(f"   bone {b.name:28} parent={par:20} head=({hx:.3f},{hy:.3f},{hz:.3f}) tail=({tx:.3f},{ty:.3f},{tz:.3f})")

print("\n=== SCENE BOUNDS / UNIT ===")
sc = bpy.context.scene
print("unit_system:", sc.unit_settings.system, "scale_length:", sc.unit_settings.scale_length)
print("frame_start/end:", sc.frame_start, sc.frame_end)
'''

r = blender_exec(CODE)
print(json.dumps(r, indent=2)[:6000])
