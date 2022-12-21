import pprint

# pprint => 보기 좋게 줄바꿈 처리
pprint.pprint(locals())

# locals() => 모든 로컬 변수를 출력해주기에 디버깅에 도움이된다
# 출력화면
# ====================================================================
# {'__annotations__': {},
#  '__builtins__': <module 'builtins' (built-in)>,
#  '__doc__': None,
#  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,       
#  '__name__': '__main__',
#  '__package__': None,
#  '__spec__': None,
#  'pprint': <module 'pprint' from 'C:\\Python311\\Lib\\pprint.py'>}
# ====================================================================
