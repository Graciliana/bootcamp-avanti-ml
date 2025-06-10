import streamlit as st
import base64

# === CONFIGURAÇÃO DE PÁGINA ===
st.set_page_config(page_title="Atividade 01 - ML", layout="centered")


# === FUNÇÃO PARA INSERIR IMAGEM DE FUNDO COM CAMADA DE CONTRASTE ===
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)),
                                  url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-attachment: fixed;
                background-repeat: no-repeat;
            }}
            summary {{
                font-size: 28px !important;
                color: #7758c2;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )


add_bg_from_local("../image/clarisse-croset--tikpxRBcsA-unsplash.jpg")

# === TÍTULOS ===
st.markdown(
    "<h1 style='color: #7758c2 ; text-align:center'>🧠 Atividade 01 - Machine Learning</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h2 style='color: #7758c2 ; text-align:center'>Questões</h2>",
    unsafe_allow_html=True,
)

# === QUESTÕES ===

# Questão 1
st.markdown(
    """
    <h2 style='color: #7758c2;'>1️⃣ O que é Machine Learning?</h2>

    <p style='color: #7758c2; font-size: 20px;'>
    Machine Learning é uma área da inteligência artificial que permite que os sistemas aprendam a realizar tarefas com base em dados, identificando padrões e fazendo predições.
    Em vez de seguir regras fixas, os modelos aprendem com exemplos passados e melhoram seu desempenho com o tempo.
    </p>

    <h3 style='color: #7758c2;'>Exemplos de aplicação:</h3>
    <ul style='color: #7758c2; font-size: 20px;'>
        <li>📦 Previsão de compras com base no histórico do cliente</li>
        <li>🎵 Sistemas de recomendação de produtos, músicas, vídeos e livros</li>
        <li>📧 Classificação de e-mails como spam ou legítimos</li>
        <li>🧠 Diagnóstico médico auxiliando na detecção de doenças</li>
        <li>📷 Reconhecimento facial em imagens e vídeos</li>
        <li>🚗 Carros autônomos tomando decisões em tempo real</li>
        <li>🖼️ Google Fotos identificando objetos, rostos e lugares automaticamente</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

# Questão 2
st.markdown(
    """
    <h2 style='color: #7758c2;'>2️⃣ O que são conjunto de treinamento, validação e teste?</h2>

    <p style='color: #7758c2; font-size: 20px;'>
    Em Machine Learning, os dados são normalmente divididos em três conjuntos principais com funções distintas:
    </p>

    <ul style='color: #7758c2; font-size: 20px;'>
        <li><strong>Conjunto de treinamento (training set):</strong> usado para ensinar o modelo. O algoritmo ajusta seus parâmetros com base nesses dados.</li>
        <li><strong>Conjunto de validação (validation set):</strong> usado durante o treinamento para ajustar hiperparâmetros e evitar overfitting.</li>
        <li><strong>Conjunto de teste (test set):</strong> usado apenas no final para avaliar o desempenho real do modelo com dados que ele nunca viu.</li>
    </ul>

    <h3 style='color: #7758c2;'>Exemplos práticos:</h3>
    <ul style='color: #7758c2; font-size: 20px;'>
        <li>🛒 Previsão de vendas com dados de compras passadas (treino), clientes recentes (validação) e novos clientes (teste).</li>
        <li>🩺 Diagnóstico médico com exames históricos (treino), exames recentes (validação) e exames de novos pacientes (teste).</li>
        <li>📷 Reconhecimento facial com imagens rotuladas (treino), rostos diferentes (validação) e pessoas nunca vistas (teste).</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

# Questão 3
st.markdown(
    """
    <h2 style='color: #7758c2;'>3️⃣ Como lidar com dados ausentes?</h2>

    <p style='color: #7758c2; font-size: 20px;'>
    Dados ausentes são comuns em projetos de Machine Learning. Se não forem tratados corretamente, podem prejudicar a performance do modelo.
    </p>

    <h3 style='color: #7758c2;'>Principais estratégias:</h3>
    <ul style='color: #7758c2; font-size: 20px;'>
        <li>❌ <strong>Remoção:</strong> excluir linhas ou colunas com poucos dados.</li>
        <li>➕ <strong>Imputação estatística:</strong> preencher com média, mediana ou moda.</li>
        <li>🧠 <strong>Imputação avançada:</strong> usar algoritmos como KNN ou regressão.</li>
        <li>🕵️ <strong>Valor constante:</strong> preencher com valores como “Desconhecido” ou 0.</li>
        <li>⚠️ <strong>Indicador:</strong> criar uma nova coluna indicando dados ausentes.</li>
    </ul>

    <h3 style='color: #7758c2;'>Exemplos:</h3>
    <ul style='color: #7758c2; font-size: 20px;'>
        <li>🏥 Preencher idade ausente com a média dos pacientes.</li>
        <li>🏠 Colocar “Sem garagem” para casas com valor de garagem ausente.</li>
        <li>🛍️ Preencher descrição de produto com “Não informada”.</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

# Questão 4
st.markdown(
    """
    <h2 style='color: #7758c2;'>4️⃣ O que é uma matriz de confusão e como ela é usada para avaliar um modelo preditivo?</h2>

    <p style='color: #7758c2; font-size: 20px;'>
    A matriz de confusão mostra a quantidade de acertos e erros de um modelo de classificação. Ela é composta por:
    </p>

    <ul style='color: #7758c2; font-size: 20px;'>
        <li><strong>Verdadeiro Positivo (VP):</strong> modelo acertou ao prever “positivo”.</li>
        <li><strong>Falso Positivo (FP):</strong> modelo errou ao prever “positivo”.</li>
        <li><strong>Verdadeiro Negativo (VN):</strong> modelo acertou ao prever “negativo”.</li>
        <li><strong>Falso Negativo (FN):</strong> modelo errou ao prever “negativo”.</li>
    </ul>

    <h3 style='color: #7758c2;'>Métricas derivadas:</h3>
    <ul style='color: #7758c2; font-size: 20px;'>
        <li>🎯 <strong>Acurácia:</strong> taxa total de acertos.</li>
        <li>💡 <strong>Precisão:</strong> taxa de acertos entre os positivos previstos.</li>
        <li>🔍 <strong>Recall:</strong> taxa de acertos entre os reais positivos.</li>
        <li>⚖️ <strong>F1-score:</strong> equilíbrio entre precisão e recall.</li>
    </ul>

    <h3 style='color: #7758c2;'>Exemplo:</h3>
    <ul style='color: #7758c2; font-size: 20px;'>
        <li>📧 <strong>VP:</strong> Spam identificado corretamente como spam.</li>
        <li>📧 <strong>FP:</strong> E-mail legítimo classificado como spam.</li>
        <li>📧 <strong>VN:</strong> E-mail legítimo corretamente identificado.</li>
        <li>📧 <strong>FN:</strong> Spam que passou como e-mail legítimo.</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

# Questão 5
st.markdown(
    """
    <h2 style='color: #7758c2;'>5️⃣ Em quais áreas é mais interessante aplicar algoritmos de Machine Learning?</h2>

    <p style='color: #7758c2; font-size: 20px;'>
    O Machine Learning pode ser aplicado em diversas áreas com grandes volumes de dados e necessidade de automação inteligente.
    </p>

    <h3 style='color: #7758c2;'>Áreas promissoras:</h3>
    <ul style='color: #7758c2; font-size: 20px;'>
        <li>🏥 <strong>Saúde:</strong> Diagnóstico, exames, tratamento personalizado.</li>
        <li>🌾 <strong>Agricultura:</strong> Previsão de safra, pragas, irrigação inteligente.</li>
        <li>🏗️ <strong>Construção:</strong> Atrasos, riscos estruturais, otimização de recursos.</li>
        <li>🏭 <strong>Manufatura:</strong> Manutenção preditiva, controle de qualidade.</li>
        <li>🛒 <strong>Comércio:</strong> Recomendação de produtos, precificação dinâmica.</li>
        <li>🚗 <strong>Transporte:</strong> Logística, carros autônomos, previsão de tráfego.</li>
        <li>💼 <strong>Finanças:</strong> Detecção de fraudes, crédito e investimentos.</li>
    </ul>

    <h3 style='color: #7758c2;'>💡 Conclusão:</h3>
    <p style='color: #7758c2; font-size: 18px;'>
    Machine Learning é uma tecnologia essencial em setores que buscam eficiência, precisão e tomada de decisão baseada em dados.
    </p>
    """,
    unsafe_allow_html=True,
)
