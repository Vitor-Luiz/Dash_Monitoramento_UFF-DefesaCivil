#Monitoramento Vitor Luiz
import plotly.io as pio
import oficial_func as of

#Importa os dados

df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")
#Mais 10 locais de sensores
df_Local_1 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_2 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_3 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_4 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_5 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_6 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_7 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_8 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_9 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_10 = of.importa_df("https://thingspeak.com/channels/1962136/")

#Definir Alarmes

#Alarmes UFF
# Alarme ACeT 
# Alarme U123
alarmeUFF_ACeT = of.alarme_ACeT(df_UFF)
alarmeUFF_U123 = of.alarme_U123(df_UFF, 30, 10, -6, "Umidade3")

#Alarmes Jurujuba L1
# Alarme ACeT 
# Alarme U123
alarmeJL1_ACeT = of.alarme_ACeT(df_Jurujuba_L1)
alarmeJL1_U123 = of.alarme_U123(df_Jurujuba_L1, 30, 10, -6, "Umidade3")

#Alarmes Jurujuba L2
# Alarme ACeT 
# Alarme U123
alarmeJL2_ACeT = of.alarme_ACeT(df_Jurujuba_L2)
alarmeJL2_U123 = of.alarme_U123(df_Jurujuba_L2, 30, 10, -6, "Umidade3")

#Alarmes Jurujuba L3
# Alarme ACeT 
# Alarme U123
alarmeJL3_ACeT = of.alarme_ACeT(df_Jurujuba_L3)
alarmeJL3_U123 = of.alarme_U123(df_Jurujuba_L3, 30, 10, -6, "Umidade3")

#Alarmes Local1
# Alarme ACeT 
# Alarme U123
alarmeL1_ACeT = of.alarme_ACeT(df_Local_1)
alarmeL1_U123 = of.alarme_U123(df_Local_1, 30, 10, -6, "Umidade3")

#Alarmes Local2
# Alarme ACeT 
# Alarme U123
alarmeL2_ACeT = of.alarme_ACeT(df_Local_2)
alarmeL2_U123 = of.alarme_U123(df_Local_2, 30, 10, -6, "Umidade3")

#Alarmes Local3
# Alarme ACeT 
# Alarme U123
alarmeL3_ACeT = of.alarme_ACeT(df_Local_3)
alarmeL3_U123 = of.alarme_U123(df_Local_3, 30, 10, -6, "Umidade3")

#Alarmes Local4
# Alarme ACeT 
# Alarme U123
alarmeL4_ACeT = of.alarme_ACeT(df_Local_4)
alarmeL4_U123 = of.alarme_U123(df_Local_4, 30, 10, -6, "Umidade3")

#Alarmes Local5
# Alarme ACeT 
# Alarme U123
alarmeL5_ACeT = of.alarme_ACeT(df_Local_5)
alarmeL5_U123 = of.alarme_U123(df_Local_5, 30, 10, -6, "Umidade3")

#Alarmes Local6
# Alarme ACeT 
# Alarme U123
alarmeL6_ACeT = of.alarme_ACeT(df_Local_6)
alarmeL6_U123 = of.alarme_U123(df_Local_6, 30, 10, -6, "Umidade3")

#Alarmes Local7
# Alarme ACeT 
# Alarme U123
alarmeL7_ACeT = of.alarme_ACeT(df_Local_7)
alarmeL7_U123 = of.alarme_U123(df_Local_7, 30, 10, -6, "Umidade3")

#Alarmes Local8
# Alarme ACeT 
# Alarme U123
alarmeL8_ACeT = of.alarme_ACeT(df_Local_8)
alarmeL8_U123 = of.alarme_U123(df_Local_8, 30, 10, -6, "Umidade3")

#Alarmes Local9
# Alarme ACeT 
# Alarme U123
alarmeL9_ACeT = of.alarme_ACeT(df_Local_9)
alarmeL9_U123 = of.alarme_U123(df_Local_9, 30, 10, -6, "Umidade3")

#Alarmes Local10
# Alarme ACeT 
# Alarme U123
alarmeL10_ACeT = of.alarme_ACeT(df_Local_10)
alarmeL10_U123 = of.alarme_U123(df_Local_10, 30, 10, -6, "Umidade3")

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
#Gráficos Local 1
figuraL1_ACeT = of.graficos_df_ACeT(df_Local_1)
figuraL1_U123 = of.graficos_df_U123(df_Local_1)
#Gráficos Local 2
figuraL2_ACeT = of.graficos_df_ACeT(df_Local_2)
figuraL2_U123 = of.graficos_df_U123(df_Local_2)
#Gráficos Local 3
figuraL3_ACeT = of.graficos_df_ACeT(df_Local_3)
figuraL3_U123 = of.graficos_df_U123(df_Local_3)
#Gráficos Local 4
figuraL4_ACeT = of.graficos_df_ACeT(df_Local_4)
figuraL4_U123 = of.graficos_df_U123(df_Local_4)
#Gráficos Local 5
figuraL5_ACeT = of.graficos_df_ACeT(df_Local_5)
figuraL5_U123 = of.graficos_df_U123(df_Local_5)
#Gráficos Local 6
figuraL6_ACeT = of.graficos_df_ACeT(df_Local_6)
figuraL6_U123 = of.graficos_df_U123(df_Local_6)
#Gráficos Local 7
figuraL7_ACeT = of.graficos_df_ACeT(df_Local_7)
figuraL7_U123 = of.graficos_df_U123(df_Local_7)
#Gráficos Local 8
figuraL8_ACeT = of.graficos_df_ACeT(df_Local_8)
figuraL8_U123 = of.graficos_df_U123(df_Local_8)
#Gráficos Local 9
figuraL9_ACeT = of.graficos_df_ACeT(df_Local_9)
figuraL9_U123 = of.graficos_df_U123(df_Local_9)
#Gráficos Local 10
figuraL10_ACeT = of.graficos_df_ACeT(df_Local_10)
figuraL10_U123 = of.graficos_df_U123(df_Local_10)

#DataFrame para o mapa
df_mapa = {"latitude":[-22.903936,-22.903937,-22.935979,-22.935980,-22.936045,-22.936046,-22.937911,-22.937912,
                       -22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,
                       -22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979],
           "longitude":[-43.133884,-43.133885,-43.109102,-43.109103,-43.109104,-43.109105,-43.107782,-43.107783,
                        -43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,
                        -43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131],
           "Sinais de Alerta":["UFF ACeT", "UFF U123", "Jurujuba1 ACeT", "Jurujuba1 U123",
                               "Jurujuba2 ACeT", "Jurujuba2 U123", "Jurujuba3 ACeT", "Jurujuba3 U123",
                               "Local1 ACeT", "Local1 U123", "Local2 ACeT", "Local2 U123", "Local3 ACeT", "Local3 U123",
                               "Local4 ACeT", "Local4 U123", "Local5 ACeT", "Local5 U123", "Local6 ACeT", "Local6 U123",
                               "Local7 ACeT", "Local7 U123", "Local8 ACeT", "Local8 U123", "Local9 ACeT", "Local9 U123",
                               "Local10 ACeT", "Local10 U123"]}

#Mapa de Monitoramento dos Alarmes
figura_mapa = of.grafico_df_mapa(df_mapa)

print("FIM")