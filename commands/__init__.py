from .online import _register_online
from .test import _register_test
from .help import _register_help
from .showbuild import _register_showbuild
from .preferences import _register_preferences
from .gxp import _register_gxp
from .plot import _register_plot
from .activity import _register_activity
from .profile import _register_profile
from .coin import _register_coin
from .ticket import _register_ticket
from .pm import _register_pm
from .join import _register_join
from .plot2 import _register_plot2
from .avg import _register_avg
from .link import _register_link
from .leaderboard import _register_leaderboard
from .map import _register_map
from .coolness import _register_coolness
from .uniform import _register_uniform
from .up import _register_up
from .glist import _register_glist
from .nuke import _register_nuke
from .alliance import _register_alliance
from .ffa import _register_ffa
from .info import _register_info
from .history import _register_history
from .warcount import _register_warcount
from .rank import _register_rank
from .wipe import _register_wipe
from valor import Valor
from discord.ext.commands.hybrid import HybridCommand

async def register_all(valor: Valor):
    """
    Registers all the commands"
    """
    await _register_help(valor)
    await _register_online(valor)
    await _register_test(valor)
    await _register_showbuild(valor)
    await _register_preferences(valor)
    await _register_gxp(valor)
    await _register_plot(valor)
    await _register_activity(valor)
    await _register_profile(valor)
    await _register_coin(valor)
    await _register_ticket(valor)
    await _register_pm(valor)
    await _register_join(valor)
    await _register_plot2(valor)
    await _register_avg(valor)
    await _register_link(valor)
    await _register_leaderboard(valor)
    await _register_coolness(valor)
    await _register_uniform(valor)
    await _register_up(valor)
    await _register_glist(valor)
    await _register_nuke(valor)
    await _register_alliance(valor)
    await _register_ffa(valor)
    await _register_info(valor)
    await _register_history(valor)
    await _register_warcount(valor)
    await _register_map(valor)
    await _register_rank(valor)
    await _register_wipe(valor)