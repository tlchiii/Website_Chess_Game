function loadPage(page) {
    fetch(`/${page}.html`)
        .then(res => res.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;
            if (page === 'accounts') loadAccounts();
            if (page === 'matches') loadMatches();
            if (page === 'posts') loadPosts();
        });
}
