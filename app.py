import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib

# Define o backend para o Matplotlib funcionar dentro do Kivy
matplotlib.use('Agg')

class Dashboard(Screen):
    def on_kv_post(self, base_widget):
        self.renderizar_graficos()

    def renderizar_graficos(self):
        # --- Gráfico de Linha (Evolução por Bimestre) ---
        fig_line, ax_line = plt.subplots(figsize=(5, 3))
        bimestres = ['1º Bi', '2º Bi', '3º Bi', '4º Bi', 'Final']
        notas = [6.5, 8.0, 5.5, 7.8, 9.0]
        
        ax_line.plot(bimestres, notas, color='red', marker='o', linewidth=2)
        ax_line.set_title("Evolução Acadêmica", fontsize=10)
        ax_line.grid(True, linestyle='--', alpha=0.6)
        
        # Adiciona ao container no KV
        self.ids.grafico_linha.add_widget(FigureCanvasKivyAgg(fig_line))

        # --- Gráfico de Barras (Frequência Mensal) ---
        fig_bar, ax_bar = plt.subplots(figsize=(5, 2))
        meses = ['Fev', 'Mar', 'Abr', 'Mai']
        frequencia = [95, 88, 70, 92]
        
        ax_bar.bar(meses, frequencia, color='blue', alpha=0.7)
        ax_bar.set_title("Frequência Mensal (%)", fontsize=10)
        ax_bar.set_ylim(0, 100)
        
        # Adiciona ao container no KV
        self.ids.grafico_barra.add_widget(FigureCanvasKivyAgg(fig_bar))

class StudentDashboardApp(App):
    def build(self):
        # Carrega o arquivo de design
        return Builder.load_file('dash.kv')

if __name__ == '__main__':
    StudentDashboardApp().run()
