Durante a execução da atividade, o ambiente local (Docker Desktop/WSL2) apresentou falha crítica de inicialização ("Docker Desktop is unable to start"), impossibilitando a captura de prints da execução em container. No entanto, a lógica de comunicação e tratamento de erros foi implementada conforme os requisitos.

Nesse tipo de implementação, quais problemas podem ocorrer?

Problema 1: Se o serviço de Produtos cair, o Estoque para de funcionar.

Problema 2 (Acoplamento): O Estoque precisa saber a URL exata do outro serviço.

Problema 3: Se o Produtos ficar lento, o Estoque trava esperando a resposta, gerando um efeito cascata.
