<template>
    <div id="viewPostWrapper">
        <div style="background-color: #cf5947; margin-left:15%; margin-right:15%; margin-top:10px;height:850px">
            <div style=" float:left; margin-top:20px; margin-left:20px; background-color: #A92C11; border-radius: 10px">
                <div style="width:500px; padding-top:10px; padding-right:20px; padding-left:10px;margin-bottom:10px; display:grid">
                    <h3 style="font-family: Roboto">{{ post.titulo }}</h3>
                    <small>Categorias: {{ categorias }}</small>
                    <small >Autor:{{ criador.nome }}</small>
                </div>
            </div>
            <div style="text-align:right; padding-top:20px; padding-right:20px;">
                 <button class="btn" style="background-color: #3ED7A7;">Favoritar post</button>
            </div>
            <div style="clear: left; margin-left:20px">
                <br/>
                <img v-bind:src="post.imagem" alt="pic" style=" width:700px; height:200px; border-radius: 10px; margin-bottom:10px;"/>
                <br/>

                <div style="background-color: #A92C11;display: inline-block; border-radius: 10px">
                    <div style="background-color:#D75A3E; margin:5px; padding:5px; border-radius: 5px">
                        <p>{{ post.conteudo }}</p>
                    </div>
                </div>
            </div>
            <div style="background:black; height:10px;margin:10px;margin-top:30px; border-radius: 20px"/>
            <div v-for="comentario in this.comentarios" :key="comentario"   style="margin-left:20px; margin-top:20px;">
                <p>{{ comentario }}</p>
                 <div style="background:gray; height:2px;margin-right:20px;border-radius: 20px"/>
            </div>
            <div style="margin-left:20px; margin-top:20px;">
                <form v-on:submit.prevent="onSubmit">
                    <h3 style="font-weight:bold;margin-bottom:10px">Deixe tambem seu comentario:</h3>
                    <textarea  placeholder="Comentario" v-model="post.nome" style="width:500px; height:100px; border-radius:10px"/>
                    <br/>
                    <br/>
                    <button class="btn btn-success" style="margin-left:5px; width:150px; height:50px" >Comentar</button>
                </form>     
            </div>
        </div>
       
    </div>
</template>

<script>
export default {
    name: 'ViewPost',
    data(){
    return {
        //img :"https://i.kym-cdn.com/entries/icons/original/000/022/713/MonkaSSS.jpg",
        post:{}, 
        criador:{},
        categorias:[],
        comentarios: [],
        //TODO: pegar esse post de forma dinamica, quando o usario clicar no ir para post em alguma das paginas de todos posts, posts da categoria ou posts da pessoa
        postId: 10,
        }
    },
    async created(){
        this.getPostAndInfo();
    },
    methods:{
        async getPostAndInfo(){
            var response = await fetch(`http://127.0.0.1:8000/api/post/${this.postId}`);
            this.post = await response.json();

            let usrs =  await fetch(`http://127.0.0.1:8000/api/usuario`)
            usrs = await usrs.json()

            var coments = await fetch(`http://127.0.0.1:8000/api/comentario`);
            coments = await coments.json()
            
            coments.forEach(coment => {
                if (coment.post == this.postId)
                {
                    let string = ""
                    for (let index = 0; index < usrs.length; index++) 
                    {
                        const element = usrs[index];
                        if (element.id == coment.criador)
                        {
                            string = coment.comentario + " -- by: " + element.nome
                        }
                    }
                    this.comentarios.push(string)
                }
            });

            var usr = await fetch(`http://127.0.0.1:8000/api/usuario/${this.post.criador}`)
            this.criador = await usr.json()

            var catIds = this.post.categorias
            for (let index = 0; index < catIds.length; index++) {
                const id = catIds[index];
                let cat_temp = await fetch(`http://127.0.0.1:8000/api/categoria/${id}`)
                cat_temp = await cat_temp.json()
                this.categorias.push(cat_temp.nome)                
            }
    
        },
    }
}
</script>
