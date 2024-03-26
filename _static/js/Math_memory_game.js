// Global variables to track game state
var BoxOpened = ""; // ID of the first opened card
var ImgOpened = ""; // Image source of the first opened card
var Counter = 0;    // Number of player moves
var ImgFound = 0;   // Number of matching pairs found
var BoxesSolved = 0; // Number of boxes solved
var Max_boxes = 2 // Number of boxes to solve to complete the game TODO: change to 4 or make it dynamic
let game_field_name = js_vars.game_field_name;


var Source = "#boxcard"; // Selector for the card container element

var ImgSource = [
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/3_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/3_part_1_smallest.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/3_part_2.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/3_part_1.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/4_part_2.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/4_part_1.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/5_part_2.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/5_part_1.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/7_part_2.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/7_part_2.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/9_part_2.png",
  // "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/9_part_2.png",
];

var ImgSource2 = [
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/11_part_3.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/11_part_4.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/12_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/12_part_2.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/15_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/15_part_2.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/16_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/16_part_2.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/3_part_3.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/3_part_4.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/4_part_3.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/4_part_4.png",
]

function isImageMatch(imgSrc1, imgSrc2) {
  const baseName1 = imgSrc1.split('/').slice(-1)[0].split('_part')[0]; 
  const baseName2 = imgSrc2.split('/').slice(-1)[0].split('_part')[0]; 
  return baseName1 === baseName2; 
}


// Helper function to generate random numbers
function RandomFunction(MaxValue, MinValue) {
		return Math.round(Math.random() * (MaxValue - MinValue) + MinValue);
	}
	
// Function to shuffle card images
function ShuffleImages() {
	var ImgAll = $(Source).children();
	var ImgThis = $(Source + " div:first-child");
	var ImgArr = new Array();
  // Store image sources in the temporary array
	for (var i = 0; i < ImgAll.length; i++) {
		ImgArr[i] = $("#" + ImgThis.attr("id") + " img").attr("src");
		ImgThis = ImgThis.next(); // Move to the next card
	}
	
		ImgThis = $(Source + " div:first-child"); // Reset to the first card
  // Shuffle the image sources and reassign them to cards
	for (var z = 0; z < ImgAll.length; z++) {
	var RandomNumber = RandomFunction(0, ImgArr.length - 1);

		$("#" + ImgThis.attr("id") + " img").attr("src", ImgArr[RandomNumber]);
		ImgArr.splice(RandomNumber, 1); // Remove the used image source
		ImgThis = ImgThis.next(); // Move to the next card
	}
}

function resetGame(){
  ImgFound = 0;
  Counter = 0;
  $("#counter").html(""); // Clear the counter
  $(Source).empty();        // Remove existing cards
 
  // Display transition message
  $("#transitionMessage").text("You completed the first box. Displaying the next box...");
  $("#transitionMessage").show();

  setTimeout(function() {
    $("#transitionMessage").hide();
      // Regenerate grid using ImgSource2 
      for (var y = 1; y < 3 ; y++) {
        $.each(ImgSource2, function(i, val) {
          $(Source).append("<div id=card" + y + i + "><img src=" + val + " />");
        });
      }
      $(Source + " div").click(OpenCard); 
      ShuffleImages(); // Shuffle the new images
      revealAllCards();
      setTimeout(function() { 
        hideAllCards();  
        $(Source + " div").click(OpenCard); 
      }, 2000); // 2-second preview
    }
  , 2000); // 2-second delay before next box (i.e. before the new grid is displayed)
  }

  // Function to handle card clicks
function OpenCard() {
	var id = $(this).attr("id"); // Get the ID of the clicked card

	if ($("#" + id + " img").is(":hidden")) {
		$(Source + " div").unbind("click", OpenCard); // Temporarily disable clicks
	
		$("#" + id + " img").slideDown('fast'); // Reveal the card

		if (ImgOpened == "") { // First card of a turn
      BoxOpened = id;
      ImgOpened = $("#" + id + " img").attr("src");
      setTimeout(function() {
        $(Source + " div").bind("click", OpenCard) // Re-enable clicks after delay
      }, 300);
    } else { // Second card of a turn
      CurrentOpened = $("#" + id + " img").attr("src");

      if (isImageMatch(ImgOpened, CurrentOpened)) { // Cards don't match
        setTimeout(function() {
          $("#" + id + " img").slideUp('fast');
          $("#" + BoxOpened + " img").slideUp('fast');
          BoxOpened = "";
          ImgOpened = "";
        }, 400);
      } else { // Cards match
        $("#" + id + " img").parent().css("visibility", "hidden");
        $("#" + BoxOpened + " img").parent().css("visibility", "hidden");
        ImgFound++;
        BoxOpened = "";
        ImgOpened = "";
      }

      setTimeout(function() {
        $(Source + " div").bind("click", OpenCard) // Re-enable clicks after delay
      }, 400);
    } 

    Counter++;
    $("#counter").html("" + Counter); 
    
    // get the num_images from the html and change its value to ImgFound
    document.getElementById(game_field_name).value = ImgFound;


    if (ImgFound == ImgSource.length) {
      if (BoxesSolved == Max_boxes-1) {
        $("#transitionMessage").text("You completed all the boxes and finished this round before timer ran out! Congratulations!");
        $("#transitionMessage").show();
      }
      else {
        BoxesSolved++;
        resetGame(); 
      }
    }
  }
}



$(function() {
  // Generate the card grid
for (var y = 1; y < 3 ; y++) {
	$.each(ImgSource, function(i, val) {
		$(Source).append("<div id=card" + y + i + "><img src=" + val + " />");
	});
}
	$(Source + " div").click(OpenCard);
	ShuffleImages();
});