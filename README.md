# Detecção de Mão e Distância da Câmera

**Autor:** Diego dos Santos Gonçalves
**Repositório:** [GitHub](https://github.com/diegobda)

Este projeto utiliza **OpenCV** e o módulo **cvzone.HandTrackingModule** para detectar a mão em tempo real e estimar a distância aproximada entre a câmera e a mão.

---

## Funcionalidades

* Detecta a mão usando **HandDetector**.
* Desenha um **bounding box** ao redor da mão.
* Calcula a **distância aproximada** da câmera até a mão (em cm).
* Atualização em tempo real com a câmera do computador.
* Encerra o programa ao pressionar a tecla `q`.

---

## Pré-requisitos

* Python 3.8+
* OpenCV
* CvZone

Instale as dependências:

```bash
pip install opencv-python cvzone
```

---

## Uso

1. Clone o repositório:

```bash
git clone https://github.com/diegobda/mao_distancia_angulo.git
cd mao_distancia_angulo
```

2. Execute o script:

```bash
python mao_distancia_angulo.py
```

3. Uma janela será aberta mostrando a câmera com a mão detectada e a distância estimada.
4. Pressione `q` para fechar a janela.

---

## Imagens do Projeto

![Screenshot 1](https://raw.githubusercontent.com/diegobda/mao_distancia_angulo/main/Screenshot%20from%202025-08-26%2014-35-04.png)

![Screenshot 2](https://raw.githubusercontent.com/diegobda/mao_distancia_angulo/main/Screenshot%20from%202025-08-26%2014-55-22.png)

---

## Configurações

* `KNOWN_WIDTH`: largura média da mão em cm (ajuste conforme necessário).
* `FOCAL_LENGTH`: distância focal da câmera (ajuste conforme testes).

Exemplo:

```python
KNOWN_WIDTH = 8.0  # cm
FOCAL_LENGTH = 650  # ajuste conforme sua câmera
```

---

## Como funciona

A distância é calculada usando a fórmula:

```
distance = (KNOWN_WIDTH * FOCAL_LENGTH) / width_hand
```

Onde:

* `KNOWN_WIDTH` = largura real da mão
* `FOCAL_LENGTH` = distância focal da câmera
* `width_hand` = largura da mão detectada na imagem

---

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request para melhorias.

---

## Licença

MIT License

---

## Autor

Diego dos Santos Gonçalves
[GitHub](https://github.com/diegobda)
