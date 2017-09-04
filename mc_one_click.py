###############################################################################
#   mc-one-click: Class - One-Click Generator for Command Block Modules       #
#   Copyright (C) 2017  TransportLayer                                        #
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU Affero General Public License as published  #
#   by the Free Software Foundation, either version 3 of the License, or      #
#   (at your option) any later version.                                       #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU Affero General Public License for more details.                       #
#                                                                             #
#   You should have received a copy of the GNU Affero General Public License  #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
###############################################################################

class One_Click:
    def __init__(self, direction="east", max_x=16, max_y=255, max_z=2, prefix="GM4", name="Module", name_internal="module", version="1.0", url="http://www.gm4.co/", no_fallingsand=False):
        self.command = ''
        self.direction = direction
        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z
        self.no_fallingsand = no_fallingsand

        self.module_init = "summon falling_block ~ ~1.5 ~ {Motion:[0.0,-1.0,0.0],Block:redstone_block,DropItem:0,Time:1,Passengers:[{id:falling_block,Block:activator_rail,Time:1,DropItem:0,Passengers:[{id:commandblock_minecart,Command:\"setblock ~2 ~-2 ~ command_block facing=east replace {TrackOutput:0b,Command:\\\"summon falling_block ~ ~.5 ~ {Block:redstone_block,Motion:[0.0,0.35,0.0]}\\\"}\"}"
        self.module_close = [
            f",{{id:commandblock_minecart,Command:\"setblock ~1 ~-2 ~ wall_sign facing=west replace {{Text3:\\\"{{\\\\\\\"text\\\\\\\":\\\\\\\"Click for Info\\\\\\\"}}\\\",Text2:\\\"{{\\\\\\\"text\\\\\\\":\\\\\\\"{name}\\\\\\\",\\\\\\\"clickEvent\\\\\\\":{{\\\\\\\"action\\\\\\\":\\\\\\\"run_command\\\\\\\",\\\\\\\"value\\\\\\\":\\\\\\\"/tellraw @s {{\\\\\\\\\\\\\\\"color\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"aqua\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"text\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"[{prefix}] {name} V{version} Click for Commands, Updates & Info\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"clickEvent\\\\\\\\\\\\\\\":{{\\\\\\\\\\\\\\\"action\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"open_url\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"value\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"{url}\\\\\\\\\\\\\\\"}}}}\\\\\\\"}}}}\\\"}}\"}}",
            f",{{id:commandblock_minecart,Command:\"summon armor_stand ~2 ~-2 ~ {{NoGravity:1,Tags:[\\\"{version}\\\",{prefix}],CustomName:{prefix}_{name_internal},Small:1,Invulnerable:1}}\"}}"
            f",{{id:commandblock_minecart,Command:\"tellraw @p {{\\\"color\\\":\\\"aqua\\\",\\\"text\\\":\\\"[{prefix}] {name} successfully installed!\\\"}}\"}}"
            ",{id:commandblock_minecart,Command:\"setblock ~2 ~-1 ~ redstone_block\"}",
            ",{id:commandblock_minecart,Command:\"kill @e[type=commandblock_minecart,r=1]\"}",
            "]}]}"
        ]

    def blank(self):
        self.command = str(self.module_init)
        for part in self.module_close:
            self.command += part
        print(self.command)
