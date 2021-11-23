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
      postbyCategory:{
        entry: 'src/views/post/postByCategory/postbyCategory.js',
        template: 'public/postbyCategory.html',
        filename: 'postbyCategory.html',
        title:'Post By Category'
      }

    }
  }