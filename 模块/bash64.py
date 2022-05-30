import base64

"""
8字节码的编码方式之一，用于传输，具有不可读性
"""

te = '花果山'
ot = base64.b64encode(te.encode('utf-8'))
print(ot)

oy = base64.b64decode(ot).decode('utf-8')
print(oy)