import matplotlib.pyplot as plt

aluno = {'calc1': 2, 'poo': 10, 'so':7}

disciplinas = list(aluno.keys())
notas = list(aluno.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(disciplinas, notas, color='maroon', width=0.4)

plt.xlabel("disciplinas oferecidas")
plt.ylabel("notas obtidas")
plt.title("grafico que mostra as notas dos alunos")
plt.show()