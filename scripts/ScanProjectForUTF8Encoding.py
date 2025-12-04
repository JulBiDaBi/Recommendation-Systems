import os

root = '.'

for dirpath, dirs, files in os.walk(root):
    for f in files:
        if f.endswith('.py'):
            path = os.path.join(dirpath, f)
            try:
                with open(path, 'r', encoding='utf-8') as fp:
                    fp.read()
            except Exception as e:
                print('❌ Problème dans :', path)
                print('   ->', e)
