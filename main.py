import os
from google import genai

print("Olá! Bem-vindo ao meu chatbot de clima! faça quanquer pergunta a ele sobre o meio ambiente!")

def iniciar_chat():
    # Inicializa o cliente (ele busca automaticamente a variável GEMINI_API_KEY)
    client = genai.Client()
    
    # Cria uma sessão de chat que mantém o histórico da conversa na memória
    chat = client.chats.create(model="gemini-2.5-flash")
    
    print("🤖 Chat IA iniciado! Digite 'sair' para encerrar.\n")
    
    while True:
        try:
            # Captura a pergunta do usuário no terminal
            usuario_input = input("Você: ")
            
            # Condição de parada
            if usuario_input.strip().lower() == 'sair':
                print("🤖 Chat encerrado. Até logo!")
                break
                
            if not usuario_input.strip():
                continue
                
            # Envia a mensagem para o modelo dentro do contexto do chat
            resposta = chat.send_message(usuario_input)
            
            # Exibe a resposta da IA no terminal
            print(f"\nIA: {resposta.text}\n")
            
        except KeyboardInterrupt:
            # Trata o atalho Ctrl+C de forma amigável
            print("\n🤖 Chat encerrado de forma abrupta. Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Ocorreu um erro: {e}\n")

if __name__ == "__main__":
    iniciar_chat()
