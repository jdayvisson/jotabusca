import streamlit as st
import urllib.parse

st.set_page_config(page_title="JOTA BUSCA", layout="wide")

# CSS estilo dark brabo
st.markdown("""
    <style>
        .big-title {
            font-size: 3em;
            font-weight: bold;
            color: #f63366;
        }
        .subtext {
            font-size: 1.2em;
            color: #999;
        }
        .dork-box {
            background-color: #111827;
            color: #fff;
            padding: 0.5em 1em;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        a {
            color: #10b981;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🔥 JOTA BUSCA 🔍</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext"> Bora fuçar a internet inteira.</div>', unsafe_allow_html=True)
st.markdown("---")

info = st.text_input("🎯 Qual a informação que você quer caçar?", placeholder="Ex: João da Silva, CPF, domínio, etc...")

# Função para gerar dorks potentes
def gerar_dorks(info):
    alvos = [
        "site:linkedin.com/in", "site:facebook.com", "site:instagram.com", "site:twitter.com",
        "site:tiktok.com", "site:youtube.com", "site:github.com", "site:gitlab.com",
        "site:pastebin.com", "site:medium.com", "site:trello.com", "site:slideshare.net",
        "site:spotify.com", "site:deezer.com", "site:imgur.com", "site:jusbrasil.com.br",
        "site:gov.br", "site:diariodonordeste.verdesmares.com.br", "site:reclameaqui.com.br",
        "site:archive.org", "site:blogspot.com", "site:wordpress.com", "site:weebly.com",
        "site:globo.com", "site:uol.com.br", "site:terra.com.br", "site:estadao.com.br",
        "site:g1.globo.com", "site:olx.com.br", "site:mercadolivre.com.br", "site:zoom.com.br"
    ]

    operadores = [
        f'"{info}"',
        f'intext:"{info}"',
        f'intitle:"{info}"',
        f'inurl:"{info}"',
        f'"{info}" filetype:pdf',
        f'"{info}" filetype:xls',
        f'"{info}" filetype:doc',
        f'"{info}" filetype:txt',
        f'"{info}" filetype:csv',
        f'"{info}" filetype:log'
    ]

    dorks = []
    for alvo in alvos:
        for op in operadores:
            dorks.append(f"{alvo} {op}")
    return dorks

# Motores e URLs
motores = {
    "Google": "https://www.google.com/search?q=",
    "Bing": "https://www.bing.com/search?q=",
    "Yahoo": "https://search.yahoo.com/search?p=",
    "DuckDuckGo": "https://duckduckgo.com/?q=",
    "Baidu": "https://www.baidu.com/s?wd=",
    "Yandex": "https://yandex.com/search/?text=",
    "Shodan": "https://www.shodan.io/search?query="
}

# Gerar URLs das buscas
def gerar_buscas(info, dorks):
    resultados = {}
    for motor, base_url in motores.items():
        urls = []

        # Primeiro, busca "crua" (sem dork)
        raw_url = base_url + urllib.parse.quote(info)
        urls.append(("🔹 BUSCA PRINCIPAL", raw_url))

        # Depois, dorks completas
        for dork in dorks:
            url = base_url + urllib.parse.quote(dork)
            urls.append((dork, url))

        resultados[motor] = urls
    return resultados

# Botão principal
if st.button("🚀 GERAR AGORA"):
    if info.strip() == "":
        st.warning("⚠️ Digita alguma coisa primeiro, guerreiro!")
    else:
        dorks = gerar_dorks(info)
        resultados = gerar_buscas(info, dorks)

        total = len(motores) * (len(dorks) + 1)  # +1 pra busca crua
        st.success(f"✅ {total} buscas geradas com sucesso! Insano, irmão!")

        tabs = st.tabs(list(resultados.keys()))
        for i, motor in enumerate(resultados.keys()):
            with tabs[i]:
                for label, url in resultados[motor]:
                    st.markdown(f"""
                        <div class="dork-box">
                            🔎 <strong>{label}</strong><br>
                            👉 <a href="{url}" target="_blank">Acessar no {motor}</a>
                        </div>
                    """, unsafe_allow_html=True)
