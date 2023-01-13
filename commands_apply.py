import sys
sys.path.append("core/")
sys.path.append("internal/")

# core
from core import *

# internal
from internal import *


COMMAND_DB = {
	"join":join.Join,
	"chat":chat.Chat,
	"emote":emote.Emote,
	"color":color.Color,
	"whisper":whisper.Whisper,
	"addserver":addserver.AddServer,
	"kick":kick.Kick,
	"delserver":delserver.DelServer,

}

INTERNAL_DB = {
	"left":left.Left
}
