document.addEventListener('DOMContentLoaded', function () {
    const options = {
        threshold: 0.5
    };

    const callback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    };

    const observer = new IntersectionObserver(callback, options);

    document.querySelectorAll('.feature-block').forEach(block => {
        observer.observe(block);
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const options = {
        threshold: 0.5
    };

    const callback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    };

    const observer = new IntersectionObserver(callback, options);

    document.querySelectorAll('.feature-block').forEach(block => {
        observer.observe(block);
    });
});
