<h1>Grafos</h1>
<p>Implementação da representação dos vários tipos de grafos em Python</p>
<h2>Nós</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Nó simples</b> => "<b>No</b>"</label>
		<p>
			A classe implementada para o nó simple está no arquivo "<b>No.py</b>". <br>
			Ela possui o atributo <i>identificador</i> que pode ser tanto um inteiro quanto uma string, e um método para retornar o nó como string. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b>, sua string ficará será "[1]".
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Nó valorado</b> => "<b>NoValorado</b>"</label>
		<p>
			A classe implementada para o nó valorado está no arquivo "<b>No.py</b>". <br>
			Ela é uma extensão da classe "<b>No</b>" citada acima com o acréscimo do atributo <i>valor</i>. <br>
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b> e <i>valor</i> = <b>15</b>, sua string ficará será "[1] {15}".
		</p>
	</li>
	<li>
		<label><b>Nó arvore</b> => "<b>NoArvore</b>"</label>
		<p>
			A classe implementada para o nó de arvore está no arquivo "<b>No.py</b>". <br>
			Ela é uma extensão da classe "<b>No</b>" citada acima com o acréscimo dos atributos <i>pai</i> e <i>distancia</i>. <br>
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b>, <i>pai</i> = <b>15</b> e <i>distancia</i> = <b>2</b>, sua string ficará será "[1] {15} (2)".
		</p>
	</li>
</ul>
<h2>Arestas</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Aresta simples</b> => "<b>Aresta</b>"</label>
		<p>
			A classe implementada para a aresta simples está no arquivo "<b>Aresta.py</b>". <br>
			Ela possui dois atributos <i>origem</i> e <i>destino</i> que são referentes aos identificadores dos dois nós conexos, e um método para retornar a aresta como string. <br />
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b>, sua string ficará será "[1, 2]".
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Aresta valorada</b> => "<b>ArestaValorada</b>"</label>
		<p>
			A classe implementada para a aresta valorada está no arquivo "<b>Aresta.py</b>". <br>
			Ela é uma extensão da classe "<b>Aresta</b>" citada acima com o acréscimo do atributo <i>valor</i>. <br> 
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>.
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b> com um <i>valor</i> = <b>15</b>, sua string ficará será "[1, 2] {15}".
		</p>
	</li>
</ul>
<h2>Árvore</h2>
<h3>Tipo</h3>
<ul>
	<li>
		<label><b>Arvore simples</b> => "<b>Arvore</b>"</label>
		<p>
			A classe implementada para a arvore simples está no arquivo "<b>Arvore.py</b>". <br>
			Ela possui dois atributos <i>raiz</i> e <i>nos</i> que são referentes ao nó raiz e à lista de nos da arvore respectivamente, e um método para inserir um nó na árvore.
		</p>
		<p></p>
	</li>
</ul>
<h2>Grafos</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Grafo simples</b> => "<b>Grafo</b>"</label>
		<p>
			A classe implementada para o grafo simples está no arquivo "<b>grafo.py</b>". <br>
			Ela possui três atributos <i>nós</i>, <i>arestas</i> e arvores que são listas para armazenar os respectivos objetos do grafo. <br>
			Essa classe também possui os seguintes métodos:
			<ul>
				<li><i>getNo(identificador)</i>: método que retorna o objeto nó se o nó de <i>identificador</i> existir no grafo.</li>
				<li><i>getAresta(origem, destino)</i>: método que retorna o objeto aresta se a aresta de <i>origem</i> e <i>destino</i> existir no grafo.</li>
				<li><i>getAdj(identificador)</i>: método que retorna uma lista dos nós adjacentes do nó de <i>identificador</i>.</li>
				<li><i>insertNo(no)</i>: método que insere o <i>nó</i> passado como parâmetro no grafo.</li>
				<li><i>insertAresta(aresta)</i>: método que insere a <i>aresta</i> passada como parâmetro no grafo.</li>
				<li><i>bfs(identificador)</i>: método que retorna a arvore criada utilizando o algoritmo breadth-first search tendo como raíz o nó de <i>identificador</i>.</li>
				<li><i>printNos()</i>: método que imprime todos os nós do grafo.</li>
				<li><i>printArestas()</i>: método que imprime todas as arestas do grafo.</li>
				<li><i>str()</i>: método que imprime todo o grafo. seguindo o modelo "( <b>nó 1</b>, <b>nó 2</b>, <b>nó n</b>; <b>aresta 1</b>, <b>aresta 2</b>, <b>aresta n</b> )"</li>
			</ul>
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Grafo simples com nó valorado</b> => "<b>Grafo_NoValorado</b>"</label>
		<p>
			A classe implementada para o grafo simples com nó valorado está no arquivo "<b>grafo.py</b>". <br>
			Ela é uma extensão da classe "<b>Grafo</b>" citada acima expecializada para comportar nós valorados.
		</p>
	</li>
	<li>
		<label><b>Grafo simples com aresta valorada</b> => "<b>Grafo_ArestaValorada</b>"</label>
		<p>
			A classe implementada para o grafo simples com aresta valorada está no arquivo "<b>grafo.py</b>". <br>
			Ela é uma extensão da classe "<b>Grafo</b>" citada acima expecializada para comportar arestas valoradas.
		</p>
	</li>
	<li>
		<label><b>Grafo simples com aresta e nó valorados</b> => "<b>Grafo_Aresta_e_NoValorados</b>"</label>
		<p>
			A classe implementada para o grafo simples com aresta e nós valorados está no arquivo "<b>grafo.py</b>". <br>
			Ela é uma extensão da classe "<b>Grafo</b>" citada acima expecializada para comportar tanto arestas quanto nós valorados.
		</p>
	</li>
	<hr>
	<li>
		<label><b>Grafo direcional</b> => "<b>DiGrafo</b>"</label>
		<p>
			A classe implementada para o grafo direcional está no arquivo "<b>grafo.py</b>". <br>
			Ela é uma extensão da classe "<b>Grafo</b>" citada acima expecializada para comportar arestas direcionais.
		</p>
	</li>
	<li>
		<label><b>Grafo direcional com nó valorado</b> => "<b>DiGrafo_NoValorado</b>"</label>
		<p>
			A classe implementada para o grafo direcional com nó valorado está no arquivo "<b>grafo.py</b>". <br>
			Ela é uma extensão da classe "<b>DiGrafo</b>" citada acima expecializada para comportar nós valorados.
		</p>
	</li>
	<li>
		<label><b>Grafo direcional com aresta valorada</b> => "<b>DiGrafo_ArestaValorada</b>"</label>
		<p>
			A classe implementada para o grafo direcional com aresta valorada está no arquivo "<b>grafo.py</b>". <br>
			Ela é uma extensão da classe "<b>DiGrafo</b>" citada acima expecializada para comportar arestas valoradas.
		</p>
	</li>
	<li>
		<label><b>Grafo direcional com aresta e nó valorados</b> => "<b>DiGrafo_Aresta_e_NoValorados</b>"</label>
		<p>
			A classe implementada para o grafo direcional com aresta e nós valorados está no arquivo "<b>Digrafo.py</b>". <br>
			Ela é uma extensão da classe "<b>DiGrafo</b>" citada acima expecializada para comportar tanto arestas quanto nós valorados.
		</p>
	</li>
</ul>