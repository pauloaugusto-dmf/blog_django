function getCookie(name){
    let cookieValue = null;
    if(document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for(let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if(cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const commentForm = document.querySelector("#comment_post");

function handleSubmit(commentForm){
    commentForm.addEventListener("submit", e => {
        e.preventDefault();
        formData = new FormData(commentForm);
        comment = document.querySelector("#comment_text").value 
        post_id = document.querySelector("#post_id").value

        fetch(URL, {
            method: 'POST',
            credentials: 'same-origin', 
            headers:{
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'post_data': {
                    'comment': comment,
                    'post_id': post_id,
                }
            })
        })
        .then(response => {
            return response.json()
        })
        .then(data => {
            let dados = JSON.parse(data)
            creatHtmlPost(dados)
        })
    })
}

handleSubmit(commentForm)

function creatHtmlPost(data){
    document.getElementById("comment")
    .insertAdjacentHTML(
        'afterbegin',
        '<div class="container"><hr><p><strong>Comentado por: </strong>' + data.user + ' <time><strong>Publicado em: </strong>' + data.comment_time + '</time></p></div><div class="container"><a>' + data.comment + '</a></div>'
    )
}