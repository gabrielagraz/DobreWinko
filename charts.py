import pandas as pd
import matplotlib.pyplot as plt

class ChartGenerator:
    def __init__(self, data_file):
        self.data_file = data_file

    def generate_chart(self):
        chart_type = self.list3_var.get()
        if chart_type == "Wykres liniowy":
            self.generate_line_chart()
        elif chart_type == "Wykres słupkowy":
            self.generate_bar_chart()
        # elif chart_type == "Wykres kołowy":
        #     self.generate_pie_chart()
        elif chart_type == "Wykres punktowy":
            self.generate_scatter_chart()
        elif chart_type == "Wykres pudełkowy":
            self.generate_box_chart()

    def generate_line_chart(self):
        with open(self.data_file, 'r') as file:
            data = pd.read_csv(file, delimiter=';')
            plt.plot(data[self.list1_var.get()], data[self.list2_var.get()])
            plt.xlabel(self.list1_var.get())
            plt.ylabel(self.list2_var.get())
            plt.title('Wykres liniowy')
            plt.show()

    def generate_bar_chart(self):
        with open(self.data_file, 'r') as file:
            data = pd.read_csv(file, delimiter=';')
            plt.bar(data[self.list1_var.get()], data[self.list2_var.get()])
            plt.xlabel(self.list1_var.get())
            plt.ylabel(self.list2_var.get())
            plt.title('Wykres słupkowy')
            plt.show()

    # def generate_pie_chart(self):
    #     with open(self.data_file, 'r') as file:
    #         data = pd.read_csv(file, delimiter=';')
    #         plt.pie(data[self.list1_var.get()], labels=data[self.list2_var.get()])
    #         plt.title('Wykres kołowy')
    #         plt.show()

    def generate_scatter_chart(self):
        with open(self.data_file, 'r') as file:
            data = pd.read_csv(file, delimiter=';')
            plt.scatter(data[self.list1_var.get()], data[self.list2_var.get()])
            plt.xlabel(self.list1_var.get())
            plt.ylabel(self.list2_var.get())
            plt.title('Wykres punktowy')
            plt.show()

    def generate_box_chart(self):
        with open(self.data_file, 'r') as file:
            data = pd.read_csv(file, delimiter=';')
            plt.boxplot(data[self.list1_var.get()])
            plt.title('Wykres pudełkowy')
            plt.show()

    @staticmethod
    def get_chart_types():
        return ["Wykres liniowy", "Wykres słupkowy", "Wykres kołowy", "Wykres punktowy", "Wykres pudełkowy"]


