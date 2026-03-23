import discord
from discord.ext import commands

# Configuração de intenções (necessário para ler mensagens)
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='?', intents=intents)

# Função que contém a lógica do conteúdo
def get_plastic_tips():
    tips = [
        "Vaso de Auto-irrigação: Corte uma garrafa PET ao meio, vire a parte do bico para baixo dentro da base com um cordão de algodão passando pelo bocal.",
        "Porta-treco: Use a parte de baixo de garrafas de amaciante ou detergente, corte e decore as bordas com fita adesiva colorida.",
        "Suporte para carregar celular: Corte um frasco de shampoo vazio no formato de uma cadeirinha que pendura direto no carregador na tomada.",
        "Paleta de tinta: Use tampinhas de garrafa coladas em um pedaço de papelão rígido para separar as cores.",
        "Comedouro para pássaros: Fure uma garrafa PET lateralmente e atravesse colheres de pau para servirem de poleiro e saída para as sementes."
    ]
    return tips

@bot.event
async def on_ready():
    print(f'Bot online como {bot.user}')

@bot.command()
async def plasticdiy(ctx):
    """Envia uma lista de ideias de reciclagem de plástico"""
    tips = get_plastic_tips()
    await ctx.send("\n\n".join(tips))

bot.run("DIGITE SEU TOKEN AQUI")
