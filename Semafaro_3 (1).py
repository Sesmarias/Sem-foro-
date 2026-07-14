import streamlit as st


# App simples para demonstrar a lógica do Jogo do Semáforo 2x2.
# Objetivo: mostrar mudança de cor, alternância de jogadores e vencedor.

st.set_page_config(page_title="Semáforo 3x4", page_icon="🚦")


# Ordem das cores do jogo.
CORES = ["preto", "verde", "amarelo", "vermelho"]

# Como cada cor é mostrada no ecrã.
SIMBOLOS = {
    "preto": "⚫️ Preto",
    "verde": "🟢 Verde",
    "amarelo": "🟡 Amarelo",
    "vermelho": "🔴 Vermelho",
}

# Próxima cor de cada célula.
PROXIMA_COR = {
    "preto": "verde",
    "verde": "amarelo",
    "amarelo": "vermelho",
    "vermelho": "vermelho",
}

# Num tabuleiro 3×4, estas são todas as linhas, colunas e diagonais.
LINHAS_VENCEDORAS = [
    #linhas
    (0, 1, 2),
    (4, 5, 6),
    (8, 9, 10),
    (1, 2, 3),
    (5, 6, 7),
    (9, 10, 11),
    #colunas
    (0, 4, 8),
    (1, 5, 9),
    (2, 6, 10),
    (3, 7, 11),
    #diagonais
    (0, 5, 10),
    (1, 6, 11),
    (2, 5, 8),
    (3, 6, 9),
]


def iniciar_jogo():
    """Coloca o jogo no estado inicial."""
    st.session_state.tabuleiro = ["preto", "preto", "preto", "preto", "preto", "preto", "preto", "preto", "preto", "preto", "preto", "preto"]
    st.session_state.jogador = 1
    st.session_state.vencedor = None
    st.session_state.mensagem = None


def garantir_estado_inicial():
    """Cria o estado do jogo na primeira vez que a app abre."""
    if "tabuleiro" not in st.session_state:
        iniciar_jogo()
    st.session_state.setdefault("mensagem", None)


def verificar_vencedor():
    """Verifica se há duas células não pretas iguais numa linha, coluna ou diagonal."""
    for a, b, c in LINHAS_VENCEDORAS:
        cor_a = st.session_state.tabuleiro[a]
        cor_b = st.session_state.tabuleiro[b]
        cor_c = st.session_state.tabuleiro[c]

        if cor_a != "preto" and cor_a == cor_b == cor_c:
            return st.session_state.jogador

    return None


def jogar(posicao):
    """Executa uma jogada numa posição do tabuleiro."""
    if st.session_state.vencedor is not None:
        return

    cor_atual = st.session_state.tabuleiro[posicao]

    if cor_atual == "vermelho":
        st.session_state.mensagem = f"A célula {posicao + 1} está bloqueada. Escolha outra."
        return

    st.session_state.mensagem = None
    st.session_state.tabuleiro[posicao] = PROXIMA_COR[cor_atual]

    vencedor = verificar_vencedor()

    if vencedor is not None:
        st.session_state.vencedor = vencedor
        return

    if st.session_state.jogador == 1:
        st.session_state.jogador = 2
    else:
        st.session_state.jogador = 1


garantir_estado_inicial()

st.title("🚦 Jogo do Semáforo 3x4")
st.write("Clique numa célula para mudar a cor: preto → verde → amarelo → vermelho.")
st.write("Vence quem formar três células iguais, não pretas, numa linha, coluna ou diagonal.")

if st.session_state.vencedor is None:
    st.info(f"Vez do Jogador {st.session_state.jogador}")
else:
    st.success(f"Jogador {st.session_state.vencedor} venceu!")

if st.session_state.mensagem:
    st.warning(st.session_state.mensagem)


# Desenho simples do tabuleiro 3x4.
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[0]],
        key="celula_0",
        on_click=jogar,
        args=(0,),
        use_container_width=True,
    )

with col2:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[1]],
        key="celula_1",
        on_click=jogar,
        args=(1,),
        use_container_width=True,
    )

with col3:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[2]],
        key="celula_2",
        on_click=jogar,
        args=(2,),
        use_container_width=True,
    )

with col4:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[3]],
        key="celula_3",
        on_click=jogar,
        args=(3,),
        use_container_width=True,
    )

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[4]],
        key="celula_4",
        on_click=jogar,
        args=(4,),
        use_container_width=True,
    )

with col6:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[5]],
        key="celula_5",
        on_click=jogar,
        args=(5,),
        use_container_width=True,
    )

with col7:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[6]],
        key="celula_6",
        on_click=jogar,
        args=(6,),
        use_container_width=True,
    )

with col8:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[7]],
        key="celula_7",
        on_click=jogar,
        args=(7,),
        use_container_width=True,
    )

col9, col10, col11, col12 = st.columns(4)

with col9:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[8]],
        key="celula_8",
        on_click=jogar,
        args=(8,),
        use_container_width=True,
    )

with col10:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[9]],
        key="celula_9",
        on_click=jogar,
        args=(9,),
        use_container_width=True,
    )

with col11:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[10]],
        key="celula_10",
        on_click=jogar,
        args=(10,),
        use_container_width=True,
    )

with col12:
    st.button(
        SIMBOLOS[st.session_state.tabuleiro[11]],
        key="celula_11",
        on_click=jogar,
        args=(11,),
        use_container_width=True,
    )


st.button("Novo jogo", on_click=iniciar_jogo)
