const express = require('express');
const fs = require('fs').promises;
const path = require('path');

const app = express();
const port = 3000;

// Middleware para entender JSON no corpo das requisições
app.use(express.json());

// Caminho do arquivo JSON
const arquivoUsuarios = path.join(__dirname, 'usuarios.json');

// Função para ler os usuários
async function lerUsuarios() {
    try {
        const dados = await fs.readFile(arquivoUsuarios, 'utf8');
        return JSON.parse(dados);
    } catch (erro) {
        // Se o arquivo não existir, começa com uma lista vazia
        if (erro.code === 'ENOENT') {
            return [];
        }

        throw erro;
    }
}

// Função para salvar os usuários
async function salvarUsuarios(usuarios) {
    await fs.writeFile(
        arquivoUsuarios,
        JSON.stringify(usuarios, null, 4),
        'utf8'
    );
}

// Rota de cadastro
app.post('/cadastrar', async (req, res) => {
    const { nome, email, idade } = req.body;

    console.log("Recebendo novo cadastro:");
    console.log(`Nome: ${nome}`);
    console.log(`E-mail: ${email}`);
    console.log(`Idade: ${idade}`);

    // Validação básica
    if (!nome || !email || !idade) {
        return res.status(400).json({
            error: "Todos os campos são obrigatórios"
        });
    }

    try {
        // Lê os usuários já cadastrados
        const usuarios = await lerUsuarios();

        // Cria o novo usuário
        const novoUsuario = {
            id: usuarios.length + 1,
            nome,
            email,
            idade
        };

        // Adiciona o usuário à lista
        usuarios.push(novoUsuario);

        // Persiste no arquivo
        await salvarUsuarios(usuarios);

        console.log("Usuário cadastrado com sucesso!");

        return res.status(201).json({
            message: "Usuário cadastrado com sucesso!",
            usuario: novoUsuario
        });

    } catch (erro) {
        console.error("Erro ao salvar usuário:", erro);

        return res.status(500).json({
            error: "Erro interno do servidor"
        });
    }
});

// Rota para consultar todos os usuários
app.get('/usuarios', async (req, res) => {
    try {
        const usuarios = await lerUsuarios();

        return res.json(usuarios);

    } catch (erro) {
        console.error("Erro ao ler usuários:", erro);

        return res.status(500).json({
            error: "Erro interno do servidor"
        });
    }
});

app.listen(port, '0.0.0.0', () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});

