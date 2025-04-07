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

st.markdown('<div class="big-title">&#128293; JOTA BUSCA &#128269;</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext"> Bora fuçar a internet inteira.</div>', unsafe_allow_html=True)
st.markdown("---")

perfil = st.selectbox("🧠 Escolha o tipo de OSINT:", ["Pessoas", "Empresas", "Documentos", "Repositórios", "Vazamentos"])

info = st.text_input("#127919;🎯 Qual a informação que você quer caçar?", placeholder="Ex: João da Silva, CPF, domínio, etc...")

# Função para gerar dorks potentes
def gerar_dorks(info):
    perfis_alvos = {
        "Pessoas": [
            "site:linkedin.com/in", "site:facebook.com", "site:instagram.com", "site:twitter.com",
            "site:tiktok.com", "site:youtube.com", "site:spotify.com", "site:deezer.com"
        ],
        "Empresas": [
            "site:jusbrasil.com.br", "site:gov.br", "site:*.gov.br", "site:*.edu.br",
            "site:reclameaqui.com.br", "site:estadao.com.br", "site:g1.globo.com"
        ],
        "Documentos": [
            "site:docs.google.com", "site:drive.google.com", "site:onedrive.live.com",
            "site:dropbox.com", "site:box.com", "site:mega.nz", "site:icloud.com",
            "site:we.tl", "site:mediafire.com", "site:zippyshare.com", "site:scribd.com",
            "site:slides.com", "site:calameo.com", "site:issuu.com"
        ],
        "Repositórios": [
            "site:github.com", "site:gitlab.com", "site:bitbucket.org"
        ],
        "Vazamentos": [
            "site:pastebin.com", "site:hastebin.com", "site:controlc.com", "site:0bin.net",
            "site:termbin.com", "site:ghostbin.com", "site:justpaste.it",
            "site:grayhatwarfare.com", "site:buckets.grayhatwarfare.com", "site:exploit-db.com",
            "site:packetstormsecurity.com", "site:openbugbounty.org", "site:shodan.io",
            "site:censys.io", "site:zoomeye.org"
        ]
    }

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
        f'"{info}" filetype:log',
        f'url:"{info}"',
        f'host:"{info}"',
        f'"{info}" mime:application/pdf',
        f'"{info}" mime:application/vnd.ms-excel',
        f'"{info}" mime:application/msword',
        f'"{info}" mime:text/plain',
        f'"{info}" mime:text/csv',
        f'"{info}" mime:text/x-log',
        f'hostname:"{info}"',
        f'org:"{info}"',
        f'product:"{info}"',
        f'city:"{info}"',
        f'country:"{info}"',
        f'os:"{info}"',
        f'"{info}" port:21',
        f'"{info}" port:80',
        f'"{info}" port:443'
    ]

    alvos = perfis_alvos.get(perfil, [])
    dorks = [f"{alvo} {op}" for alvo in alvos for op in operadores]
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
        urls.append(("🔹 BUSCA PRINCIPAL", base_url + urllib.parse.quote(info)))
        for dork in dorks:
            urls.append((dork, base_url + urllib.parse.quote(dork)))
        resultados[motor] = urls
    return resultados

# Botão principal
if st.button("🚀 GERAR AGORA"):
    if info.strip() == "":
        st.warning("⚠️ Digita alguma coisa primeiro, guerreiro!")
    else:
        dorks = gerar_dorks(info)
        resultados = gerar_buscas(info, dorks)

        total = len(motores) * (len(dorks) + 1)
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
