# Projeto Python para Engenharia de Dados

## 🚀 Cenário 
A empresa acompanha os preços das ações, commodity , taxas de câmbio e taxas de inflação. A proposta do projeto é extrair dados financeiros de várias fontes, como sites, APIs e arquivos fornecidos por várias empresas de análise financeira.  Depois de coletar os dados, foram extraídos os de interesse para o projeto e transformados com base nos parâmetros fornecidos. Depois da transformação concluída, os dados foram carregados em um banco de dados. 

## 🤿 Começando 
Essas instruções permitirão que vocẽ obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.
Consultar **[Implantação] (#-implantação)** para mais detalhes de implementação do projeto. 

### 📋 Pré-requisitos
Configurações e instalação
```
sudo apt-get install python3-bs4
sudo apt-get install -y python3-html5lib

```
## 📦 Implantação
### Importações

Neste projeto foram executados os seguintes passos:
- A importação das bibliotecas para serem utilizadas 

```
from bs4 import BeautifulSoup
import requests
import pandas as pd
```

