document.addEventListener('DOMContentLoaded', function() {
    const questions = [
        // 1-25
        { q: "What is the world's most populated country?", choices: ["USA", "China", "Russia", "India"], answer: "China" },
        { q: "Who wrote 'Pride and Prejudice'?", choices: ["Charlotte Brontë", "Emily Dickinson", "Jane Austen", "Mary Shelley"], answer: "Jane Austen" },
        { q: "What is the chemical symbol for gold?", choices: ["Au", "Ag", "Gd", "Go"], answer: "Au" },
        { q: "Which planet is known as the Red Planet?", choices: ["Mars", "Jupiter", "Saturn", "Venus"], answer: "Mars" },
        { q: "The Mona Lisa is on display in which Paris museum?", choices: ["The Louvre", "Musée d'Orsay", "Centre Pompidou", "Musée Rodin"], answer: "The Louvre" },
        { q: "Who is the author of the Harry Potter series?", choices: ["J.K. Rowling", "J.R.R. Tolkien", "Stephen King", "Suzanne Collins"], answer: "J.K. Rowling" },
        { q: "Which country is the largest by land area?", choices: ["Russia", "Canada", "China", "United States"], answer: "Russia" },
        { q: "Sushi is a traditional food from which country?", choices: ["China", "Korea", "Japan", "Thailand"], answer: "Japan" },
        { q: "Who was the first woman to win a Nobel Prize (in 1903)?", choices: ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Elizabeth Blackwell"], answer: "Marie Curie" },
        { q: "The Berlin Wall fell in which year?", choices: ["1989", "1991", "1987", "1990"], answer: "1989" },
        { q: "What does 'HTTP' stand for in website addresses?", choices: ["HyperText Transfer Protocol", "High-Tech Transmission Protocol", "HyperTerminal Tracking Program", "None of the above"], answer: "HyperText Transfer Protocol" },
        { q: "Which element is named after the creator of the periodic table?", choices: ["Curium", "Einsteinium", "Mendelevium", "Nobelium"], answer: "Mendelevium" },
        { q: "What type of restaurant would you typically find the dish 'ramen'?", choices: ["Korean", "Japanese", "Thai", "Chinese"], answer: "Japanese" },
        { q: "What is the term for a word that is similar in meaning to another word?", choices: ["Antonym", "Synonym", "Homonym", "Acronym"], answer: "Synonym" },
        { q: "Which gas is the primary contributor to global warming?", choices: ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"], answer: "Carbon dioxide" },
        { q: "The concept of reducing your carbon footprint is associated with what?", choices: ["Lowering personal energy use", "Planting trees", "Recycling more waste", "All of the above"], answer: "All of the above" },
        { q: "What is the force that causes objects to fall to the ground?", choices: ["Gravity", "Electricity", "Magnetism", "Friction"], answer: "Gravity" },
        { q: "What is the value of Pi to two decimal places?", choices: ["3.14", "2.14", "3.15", "4.14"], answer: "3.14" },
        { q: "Which layer of Earth's atmosphere contains the ozone layer?", choices: ["Troposphere", "Stratosphere", "Mesosphere", "Exosphere"], answer: "Stratosphere" },
        { q: "Who composed the Four Seasons?", choices: ["Vivaldi", "Bach", "Mozart", "Beethoven"], answer: "Vivaldi" },
        { q: "Which movie won the Best Picture Oscar in 2020?", choices: ["The Irishman", "1917", "Parasite", "Joker"], answer: "Parasite" },
        { q: "Who created the fictional detective Sherlock Holmes?", choices: ["Mark Twain", "Agatha Christie", "Arthur Conan Doyle", "Charles Dickens"], answer: "Arthur Conan Doyle" },
        { q: "What is the most widely spoken language in the world by number of native speakers?", choices: ["English", "Mandarin", "Spanish", "Hindi"], answer: "Mandarin" },
        { q: "What is the most widely spoken language in the world by number of native speakers?", choices: ["English", "Mandarin", "Spanish", "Hindi"], answer: "Mandarin" },
        { q: "Who painted the Sistine Chapel ceiling?", choices: ["Michelangelo", "Raphael", "Donatello", "Leonardo da Vinci"], answer: "Michelangelo" },
        { q: "What does USB stand for when talking about a USB Flash Drive?", choices: ["Universal Serial Bus", "United System Bank", "User Service Base", "Universal System Backup"], answer: "Universal Serial Bus" },
        // 26-50
        { q: "What river is the longest in the world?", choices: ["Nile", "Amazon", "Yangtze", "Mississippi"], answer: "Nile" },
        { q: "Who was the first president of the United States?", choices: ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"], answer: "George Washington" },
        { q: "How many players are on a soccer team on the field at the same time?", choices: ["11", "9", "7", "13"], answer: "11" },
        { q: "What is the powerhouse of the cell?", choices: ["Mitochondria", "Nucleus", "Ribosome", "Endoplasmic Reticulum"], answer: "Mitochondria" },
        { q: "What galaxy is Earth located in?", choices: ["Milky Way", "Andromeda", "Galaxy B", "Whirlpool Galaxy"], answer: "Milky Way" },
        { q: "What is the common name for the medical condition of diabetes mellitus?", choices: ["Sugar", "High Blood Pressure", "Thyroid", "Cholesterol"], answer: "Sugar" },
        { q: "What is the name for the small image icons used to express emotions or ideas in digital communication?", choices: ["Emoticons", "Emails", "Emoji", "Signals"], answer: "Emoji" },
        { q: "What term describes the study of human behavior and mind?", choices: ["Psychology", "Anthropology", "Sociology", "Ecology"], answer: "Psychology" },
        { q: "Which particle is negatively charged?", choices: ["Electron", "Neutron", "Proton", "Photon"], answer: "Electron" },
        { q: "What is the main ingredient in guacamole?", choices: ["Avocado", "Tomato", "Potato", "Cucumber"], answer: "Avocado" },
        { q: "What is a common term for the decrease in the value of money?", choices: ["Inflation", "Deflation", "Recession", "Depression"], answer: "Inflation" },
        { q: "What color do you get when you mix red and blue?", choices: ["Orange", "Green", "Purple", "Pink"], answer: "Purple" },
        { q: "Which novel features a character named Scout Finch?", choices: ["To Kill a Mockingbird", "Great Expectations", "The Catcher in the Rye", "Lord of the Flies"], answer: "To Kill a Mockingbird" },
        { q: "Which ancient civilization built the pyramids?", choices: ["Mayan", "Aztec", "Egyptian", "Incan"], answer: "Egyptian" },
        { q: "What TV series is based in the fictional town of Hawkins, Indiana?", choices: ["Stranger Things", "Riverdale", "Smallville", "Euphoria"], answer: "Stranger Things" },
        { q: "What is the hardest natural substance on Earth?", choices: ["Granite", "Diamond", "Quartz", "Steel"], answer: "Diamond" },
        { q: "What is the smallest country in the world by land area?", choices: ["Vatican City", "Monaco", "Nauru", "Liechtenstein"], answer: "Vatican City" },
        { q: "Which bird is often associated with delivering babies in folklore?", choices: ["Stork", "Sparrow", "Pelican", "Swan"], answer: "Stork" },
        { q: "What musical instrument has keys, pedals, and strings?", choices: ["Piano", "Drum", "Guitar", "Trumpet"], answer: "Piano" },
        { q: "In tennis, what term is used for a score of zero?", choices: ["Love", "Fault", "Deuce", "Advantage"], answer: "Love" },
        { q: "What does AI stand for in technology?", choices: ["Automatic Input", "Artificial Intelligence", "Alternative Information", "Advanced Interface"], answer: "Artificial Intelligence" },
        { q: "What is tofu made from?", choices: ["Wheat", "Milk", "Soybeans", "Rice"], answer: "Soybeans" },
        { q: "What language is primarily spoken in Brazil?", choices: ["Spanish", "Portuguese", "French", "Italian"], answer: "Portuguese" },
        { q: "Which law states that for every action there is an equal and opposite reaction?", choices: ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Newton's Law of Gravity"], answer: "Newton's Third Law" },
        // 50-80
        { q: "Which celestial body is the center of our Solar System?", choices: ["Earth", "The Moon", "The Sun", "Jupiter"], answer: "The Sun" },
        { q: "Which common gas is formula O2?", choices: ["Hydrogen", "Nitrogen", "Carbon Dioxide", "Oxygen"], answer: "Oxygen" },
        { q: "What process do plants use to convert sunlight into food?", choices: ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"], answer: "Photosynthesis" },
        { q: "Which film director is known for movies such as 'The Grand Budapest Hotel' and 'Moonrise Kingdom'?", choices: ["Wes Anderson", "Steven Spielberg", "Quentin Tarantino", "Martin Scorsese"], answer: "Wes Anderson" },
        { q: "In which book series is the fictional continent Westeros found?", choices: ["The Wheel of Time", "The Chronicles of Narnia", "A Song of Ice and Fire", "The Lord of the Rings"], answer: "A Song of Ice and Fire" },
        { q: "Who was the first female Prime Minister of the United Kingdom?", choices: ["Margaret Thatcher", "Theresa May", "Angela Merkel", "Indira Gandhi"], answer: "Margaret Thatcher" },
        { q: "Which artist is known for the painting 'The Starry Night'?", choices: ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet"], answer: "Vincent van Gogh" },
        { q: "Which is the largest ocean on Earth?", choices: ["Atlantic", "Pacific", "Indian", "Arctic"], answer: "Pacific" },
        { q: "What is the main difference between frogs and toads?", choices: ["Skin type", "Leg length", "Eye shape", "Diet"], answer: "Skin type" },
        { q: "What is the value of the mathematical constant e rounded to two decimal places?", choices: ["2.71", "1.41", "3.14", "1.61"], answer: "2.71" },
        { q: "Who wrote the epic poem 'Paradise Lost'?", choices: ["John Milton", "William Blake", "Geoffrey Chaucer", "William Shakespeare"], answer: "John Milton" },
        { q: "In which country is the traditional Maori haka dance performed?", choices: ["Australia", "New Zealand", "Fiji", "Samoa"], answer: "New Zealand" },
        { q: "What year did the Titanic sink?", choices: ["1910", "1912", "1914", "1916"], answer: "1912" },
        { q: "What year was the World Wide Web introduced to the public?", choices: ["1989", "1991", "1993", "1995"], answer: "1991" },
        { q: "What is the regulation height for a basketball hoop?", choices: ["8 feet", "9 feet", "10 feet", "11 feet"], answer: "10 feet" },
        { q: "Which film features a character named Forrest Gump?", choices: ["Forrest Gump", "The Shawshank Redemption", "Pulp Fiction", "Schindler's List"], answer: "Forrest Gump" },
        { q: "What is the tallest mountain in the world when measured from base to summit?", choices: ["Mount Everest", "K2", "Mount Kilimanjaro", "Mauna Kea"], answer: "Mauna Kea" },
        { q: "Which vitamin is known as ascorbic acid?", choices: ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], answer: "Vitamin C" },
        { q: "What is a group of lions called?", choices: ["Pack", "Pride", "School", "Herd"], answer: "Pride" },
        { q: "Which language is known as the language of love?", choices: ["French", "Italian", "Spanish", "Portuguese"], answer: "French" },
        { q: "What is the speed of light in a vacuum?", choices: ["299,792 km/s", "299,792 m/s", "299,792 km/h", "299,792 m/h"], answer: "299,792 km/s" },
        { q: "Who directed the movie 'Inception'?", choices: ["Christopher Nolan", "Steven Spielberg", "James Cameron", "Peter Jackson"], answer: "Christopher Nolan" },
        { q: "Which primary colors are used to create all other colors?", choices: ["Red, Yellow, Blue", "Red, Green, Blue", "Yellow, Blue, Purple", "Orange, Green, Violet"], answer: "Red, Yellow, Blue" },
        { q: "What is the name of the default directory that serves as the main folder for user files in Windows?", choices: ["Documents", "My Documents", "My Files", "User Folder"], answer: "My Documents" },
        { q: "What is the currency of Japan?", choices: ["Yuan", "Yen", "Won", "Rupee"], answer: "Yen" },
        { q: "What renewable energy source is derived from the Earth's internal heat?", choices: ["Solar", "Wind", "Hydrothermal", "Geothermal"], answer: "Geothermal" },
        { q: "What is the name for the classification system used to organize living things?", choices: ["The Linnaean System", "The Dewey Decimal System", "The Darwinian System", "The Newtonian System"], answer: "The Linnaean System" },
        { q: "What is the most abundant gas in Earth's atmosphere?", choices: ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"], answer: "Nitrogen" },
        { q: "The Great Gatsby was written by which author?", choices: ["Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain", "Harper Lee"], answer: "F. Scott Fitzgerald" },
        { q: "What is the most commonly used letter in the English language?", choices: ["E", "T", "A", "S"], answer: "E" },
        { q: "Which planet is known for its rings?", choices: ["Mars", "Saturn", "Jupiter", "Venus"], answer: "Saturn" },
        // 81-100
        { q: "What is the Fibonacci sequence?", choices: ["A series of numbers where the next number is found by adding up the two numbers before it", "A series of prime numbers", "A series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1", "A series of numbers where each number is the product of the two preceding ones"], answer: "A series of numbers where the next number is found by adding up the two numbers before it" },
        { q: "Who was the first female aviator to fly solo across the Atlantic Ocean?", choices: ["Amelia Earhart", "Bessie Coleman", "Harriet Quimby", "Jean Batten"], answer: "Amelia Earhart" },
        { q: "What layer of the Earth is made up of tectonic plates?", choices: ["Crust", "Mantle", "Core", "Lithosphere"], answer: "Crust" },
        { q: "What is the term for the fear of technology?", choices: ["Cyberphobia", "Technophobia", "Robophobia", "Mechaphobia"], answer: "Technophobia" },
        { q: "Who composed the Brandenburg Concertos?", choices: ["Bach", "Beethoven", "Mozart", "Haydn"], answer: "Bach" },
        { q: "Which country is traditionally associated with paella?", choices: ["Italy", "Spain", "Mexico", "Portugal"], answer: "Spain" },
        { q: "What is the process by which plants make their food?", choices: ["Transpiration", "Photosynthesis", "Respiration", "Osmosis"], answer: "Photosynthesis" },
        { q: "What is the name of the galaxy closest to the Milky Way?", choices: ["Andromeda", "Whirlpool", "Triangulum", "Black Eye"], answer: "Andromeda" },
        { q: "What shape is the base of a cylinder?", choices: ["Triangle", "Rectangle", "Circle", "Square"], answer: "Circle" },
        { q: "Who is the Roman god of war?", choices: ["Mars", "Jupiter", "Neptune", "Vulcan"], answer: "Mars" },
        { q: "What river runs through Cairo?", choices: ["Nile", "Amazon", "Thames", "Ganges"], answer: "Nile" },
        { q: "What is the most widely spoken language in India?", choices: ["Hindi", "Bengali", "Tamil", "Marathi"], answer: "Hindi" },
        { q: "What percentage of the Earth's surface is covered by oceans?", choices: ["51%", "61%", "71%", "81%"], answer: "71%" },
        { q: "In what country were the first modern Olympic Games held?", choices: ["Greece", "France", "USA", "Italy"], answer: "Greece" },
        { q: "Which artist painted 'Guernica'?", choices: ["Picasso", "Van Gogh", "Dali", "Monet"], answer: "Picasso" },
        { q: "What is the study of meaning in language called?", choices: ["Syntax", "Semantics", "Phonology", "Morphology"], answer: "Semantics" },
        { q: "What is the main component of the sun?", choices: ["Helium", "Hydrogen", "Nitrogen", "Oxygen"], answer: "Hydrogen" },
        { q: "Which architect designed the Guggenheim Museum in Bilbao?", choices: ["Gehry", "Wright", "Gaudi", "Pei"], answer: "Gehry" },
        { q: "Who wrote 'The Republic'?", choices: ["Plato", "Aristotle", "Socrates", "Pythagoras"], answer: "Plato" },
        { q: "What vitamin is produced when a person is exposed to sunlight?", choices: ["Vitamin C", "Vitamin D", "Vitamin A", "Vitamin E"], answer: "Vitamin D" }
    ];
    
    let game_field_name = js_vars.game_field_name;
    let currentQuestion = 0;
    let timer = 10;
    let interval;

    function showQuestion() {
        // Load saved state, if exists and the page is initially loaded
        if(localStorage.getItem("currentQuestion") && currentQuestion === 0) {
            currentQuestion = parseInt(localStorage.getItem("currentQuestion"), 10);
            // Load timer only if it's not already counting down
            if (!interval) {
                timer = parseInt(localStorage.getItem("timer"), 5);
            }
        }
    
        if (currentQuestion < questions.length) {
            currentQuestion_idx = currentQuestion+1;
            MaxQuestions_idx = questions.length-1;
            document.getElementById('question').textContent = 'Question ' + currentQuestion_idx + '. '  + questions[currentQuestion].q;
            const choicesContainer = document.getElementById('choices');
            choicesContainer.innerHTML = ''; // Clear previous choices
            questions[currentQuestion].choices.forEach(function(choice) {
                const button = document.createElement('button');
                button.textContent = choice;
                button.onclick = selectAnswer;
                choicesContainer.appendChild(button);
            });
            // Update the timer display without resetting it
            document.getElementById('timer').textContent = `Time left for this question: ${timer} seconds`;
            // Only start the interval if it's not already running
            if (!interval) {
                interval = setInterval(updateTimer, 1000);
            }
        } else {
            document.getElementById('quiz-container').innerHTML = '<div>Quiz completed!</div>';
            // Clear local storage as the quiz is completed
            localStorage.removeItem("currentQuestion");
            localStorage.removeItem("timer");
        }
    }

    function selectAnswer(event) {
        const selectedAnswer = event.target.textContent;
        const correctAnswer = questions[currentQuestion].answer;
        if (selectedAnswer === correctAnswer) {
            console.log(currentQuestion,  'is Correct!');
            document.getElementById(game_field_name).value ++;
        } else {
            console.log(currentQuestion, 'is Wrong!');
        }
        moveToNextQuestion();
    }


    function updateTimer() {
        timer--;
        document.getElementById('timer').textContent = `Time left for this question: ${timer} seconds`;
        if (timer <= 0) {
            moveToNextQuestion();
        }
        // Save current state
        localStorage.setItem("currentQuestion", currentQuestion);
        localStorage.setItem("timer", timer);
    }

    function moveToNextQuestion() {
        clearInterval(interval);
        interval = null; // Clear interval ID
        currentQuestion++;
        // Reset the timer for the next question
        timer = 10;
        localStorage.setItem("currentQuestion", currentQuestion);
        localStorage.setItem("timer", timer);
        showQuestion();
    }

    showQuestion();
});
