const openTutorialButtons = document.querySelectorAll('[data-tutorial-target]') // select #tutorial .info button
const closeTutorialButtons = document.querySelectorAll('[data-close-button]') // select .close-button button
const overlay = document.getElementById('overlay') // select div with the id = 'overlay'

// creates event when clicking on "How to play" will use function openTutorial
openTutorialButtons.forEach(button => {
    button.addEventListener('click', () => {
        const tutorial = document.querySelector(button.dataset.tutorialTarget)
        openTutorial(tutorial)
    })
})

// creates event when click on "How to play" will 
overlay.addEventListener('click', () => {
    const tutorial = document.querySelectorAll('.tutorial.active')
    tutorial.forEach(tutorial => {
        closeTutorial(tutorial)
    })
})

// creates event when clicking on "x" will use function closeTutorial
closeTutorialButtons.forEach(button => {
    button.addEventListener('click', () => {
        const tutorial = button.closest('.tutorial')
        closeTutorial(tutorial)
    })
})

function openTutorial(tutorial) {
    if (tutorial == null) return
    tutorial.classList.add('active')
    overlay.classList.add('active')
}

function closeTutorial(tutorial) {
    if (tutorial == null) return
    tutorial.classList.remove('active')
    overlay.classList.remove('active')
}
