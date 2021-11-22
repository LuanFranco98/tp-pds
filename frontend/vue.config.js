module.exports = {
    // options...
    assetsDir:'static',

    outputDir:'templates',
    
    pages:{
      createPost:{
        entry: 'src/views/post/createPost/createPost.js',
        template: 'public/index.html',
        filename: 'createPost.html',
        title:'Create Post'
      },
      createUsuario:{
        entry: 'src/views/usuario/createUsuario.js',
        template: 'public/index.html',
        filename: 'createUsuario.html',
        title:'Create Usuario'
      },
      postByCategory:{
        entry: 'src/views/post/postByCategory/postByCategory.js',
        template: 'public/index.html',
        filename: 'postByCategory.html',
        title:'Post by Category'
      }

    }
  }