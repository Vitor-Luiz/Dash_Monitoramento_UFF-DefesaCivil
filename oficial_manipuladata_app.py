#Monitoramento Vitor Luiz
import plotly.io as pio
import oficial_func as of

df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")

#Definir Alarmes

#Alarmes UFF
# Alarme ACeT 
# Alarme U123
alarmeUFF_U123 = of.alarme_U123(df_UFF, 30, 10, -10, "Umidade3")

#Alarmes Jurujuba L1
# Alarme ACeT 
# Alarme U123
alarmeJL1_U123 = of.alarme_U123(df_Jurujuba_L1, 30, 10, -10, "Umidade3")

#Alarmes Jurujuba L2
# Alarme ACeT 
# Alarme U123
alarmeJL2_U123 = of.alarme_U123(df_Jurujuba_L2, 30, 10, -10, "Umidade3")

#Alarmes Jurujuba L3
# Alarme ACeT 
# Alarme U123
alarmeJL3_U123 = of.alarme_U123(df_Jurujuba_L3, 30, 10, -10, "Umidade3")

#Gráficos
pio.templates
#Gráficos UFF
figuraUFF_ACeT = of.graficos_df_ACeT(df_UFF)
figuraUFF_U123 = of.graficos_df_U123(df_UFF)
#Gráficos Jurujuba L1
figuraJL1_ACeT = of.graficos_df_ACeT(df_Jurujuba_L1)
figuraJL1_U123 = of.graficos_df_U123(df_Jurujuba_L1)
#Gráficos Jurujuba L2
figuraJL2_ACeT = of.graficos_df_ACeT(df_Jurujuba_L2)
figuraJL2_U123 = of.graficos_df_U123(df_Jurujuba_L2)
#Gráficos Jurujuba L3
figuraJL3_ACeT = of.graficos_df_ACeT(df_Jurujuba_L3)
figuraJL3_U123 = of.graficos_df_U123(df_Jurujuba_L3)

#DataFrame para o mapa
df_mapa = {"latitude":[-22.903936,-22.903937,-22.935979,-22.935980,-22.936045,-22.936046,-22.937911,-22.937912],
           "longitude":[-43.133884,-43.133885,-43.109102,-43.109103,-43.109104,-43.109105,-43.107782,-43.107783],
           "Sinais de Alerta":["UFF ACeT", "UFF U123", "Jurujuba1 ACeT", "Jurujuba1 U123",
                               "Jurujuba2 ACeT", "Jurujuba2 U123", "Jurujuba3 ACeT", "Jurujuba3 U123"]}

#Mapa de Monitoramento dos Alarmes
figura_mapa = of.grafico_df_mapa(df_mapa)

print("FIM")