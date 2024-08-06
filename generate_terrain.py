import json

terrain = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                                             @
@                                    @@@@@@@@@@@@@@@@@@@@@@@@@@
@                                   @@                        @
@                                  @@@                        @
@                                 @@@@                        @
@                                @@@@@                        @
@                               @@@@@@                        @
@                              @@@@@@@                        @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

terrain2 = """
    
"""

blocks = []

temp = terrain.strip().split("\n")


for x, row in enumerate(temp):
    row_blocks = []
    for y, block in enumerate(row):
        row_blocks.append(
            {"x": x, "y": y, "material": {" ": "air", "@": "stone"}[block]}
        )
    blocks.append(row_blocks)


print(json.dumps(blocks))
