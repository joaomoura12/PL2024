# _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado

class DataAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()
        return [line.strip().split(',') for line in lines[1:]]

    def write_to_file(self, text):
        with open("resultados.txt", "a") as output_file:
            output_file.write(text + "\n\n___________________________________\n")

    def listar_modalidades_alfabetica(self, data):
        modalities = sorted(set(entry[8] for entry in data))
        modalities_text = "\n".join(modalities)
        self.write_to_file("Lista ordenada alfabeticamente das modalidades desportivas:\n" + modalities_text)

    def clacular_percentagens(self, data):
        total_athletes = len(data)
        apt_athletes = sum(entry[12] == 'true' for entry in data)
        inapt_athletes = total_athletes - apt_athletes
        perc_apt = (apt_athletes / total_athletes) * 100
        perc_inapt = (inapt_athletes / total_athletes) * 100
        text = (f"Percentagens de atletas aptos e não aptos para a prática desportiva:\n"
                f"Percentagens de atletas aptos: {perc_apt}%\n"
                f"Percentagem de atletas inaptos: {perc_inapt}%")
        self.write_to_file(text)

    def atletas_analize(self, data):
        age_distribution = {}
        for entry in data:
            age = int(entry[5])
            interval = f"[{age // 5 * 5}-{age // 5 * 5 + 4}]"
            age_distribution[interval] = age_distribution.get(interval, 0) + 1
        text = "Distribuição de atletas por escalão etário:\n"
        for interval, quantity in sorted(age_distribution.items()):
            text += f"{interval}: {quantity}\n"
        self.write_to_file(text)

    def analyze_data(self):
        data = self.read_data()
        self.listar_modalidades_alfabetica(data)
        self.clacular_percentagens(data)
        self.atletas_analize(data)


# Executing the analysis
analyzer = DataAnalyzer("emd.csv")
analyzer.analyze_data()

