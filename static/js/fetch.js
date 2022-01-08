function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function makeRequest(url, data) {
    const init = {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
                'data': data
            })
    }
    const newRequest = new Request(url, init)
    return newRequest
}

function createCommentHTML(data) {
    document.getElementById("comment")
        .insertAdjacentHTML(
            'afterbegin',
            '<div class="container"><hr>' +
            '   <p><strong>Comentado por: </strong>' + data.user + ' ' +
            '   <time><strong>Publicado em: </strong>' + data.comment_time + '</time></p>' +
            '   </div><div class="container"><a>' + data.comment + '</a></div>'
        )
}

function createLikeDislikeHTML(data) {
    document.getElementById("like").text = data.like
    document.getElementById("dislike").text = data.dislike

}

const csrftoken = getCookie('csrftoken');


function handleSubmit(form, url){
    form.addEventListener(
        "submit",
        e => {
            e.preventDefault();

            if (e.target.id === "commentForm") {
                const comment = document.querySelector("#commentText").value
                const commentRequest = makeRequest(url, comment)
                fetch(commentRequest)
                    .then(response => {
                        return response.json()
                    })
                    .then(data =>{
                        let commentData = JSON.parse(data)
                        createCommentHTML(commentData)
                    })
            } else if (e.target.id === "likeForm") {
                const like = 1
                const likeRequest = makeRequest(url, like)
                fetch(likeRequest)
                    .then(response => {
                        return response.json()
                    })
                    .then(data =>{
                        let likeData = JSON.parse(data)
                        createLikeDislikeHTML(likeData)
                    })
            } else if (e.target.id === "dislikeForm") {
                const dislike = 0
                const dislikeRequest = makeRequest(url, dislike)
                fetch(dislikeRequest)
                    .then(response => {
                        return response.json()
                    })
                    .then(data =>{
                        let dislikeData = JSON.parse(data)
                        createLikeDislikeHTML(dislikeData)
                    })
            }
        }
    )
}



const commentForm = document.querySelector("#commentForm")
const  likeForm = document.querySelector("#likeForm")
const  dislikeForm = document.querySelector("#dislikeForm")


handleSubmit(commentForm, URL_COMMENT)
handleSubmit(likeForm, URL_LIKE)
handleSubmit(dislikeForm, URL_LIKE)