// Global variables to track game state
var BoxOpened = ""; // ID of the first opened card
var ImgOpened = ""; // Image source of the first opened card
var Counter = 0;    // Number of player moves
var ImgFound = 0;   // Number of matching pairs found
var BoxesSolved = 0; // Number of boxes solved
var Max_boxes = 4 // Number of boxes to solve to complete the game TODO: change to 4 or make it dynamic
let game_field_name = js_vars.game_field_name;
console.log('visual memory loaded')

var Source = "#boxcard"; // Selector for the card container element
// TODO: proper shuffling.
var ImgSource1 = [
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/3_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/3_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/4_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/4_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%201/5_part_1.png",
  
];
var ImgSource2 = [
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/3_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/3_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/4_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/4_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%202/11_part_1.png",
  
];
var ImgSource3 = [
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%203/5_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%203/5_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%203/6_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%203/6_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%203/10_part_1.png",
];
var ImgSource4 = [
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%204/6_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%204/6_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%204/7_part_1.png",
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%204/7_part_2.png",
 
  "https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Math_memory_boxes/Box%204/8_part_1.png",
  
];



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

function image_source() {
  if (BoxesSolved == 0) {
    return ImgSource1;
  }
  if (BoxesSolved == 1) {
    return ImgSource2;
  }
  else if (BoxesSolved == 2) {
    return ImgSource3;
  }
  else if (BoxesSolved == 3) {
    return ImgSource4;
  }
  else {
    // break out of loop and display final message
    $("#transitionMessage").text("You completed all the boxes and finished this round before timer ran out. You receive maximum points from this round! Congratulations!");
    $("#transitionMessage").show();
    return;
  }
}

function resetGame(){
  ImgSource = image_source(); // Get the image source for the current box

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
    }
  , 2000); // 2-second delay before next box (i.e. before the new grid is displayed)
  }

  // Function to handle card clicks
function OpenCard() {
	var id = $(this).attr("id"); // Get the ID of the clicked card
  ImgSource = image_source(); // Get the image source for the current box

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

      if (ImgOpened != CurrentOpened) { // Cards don't match
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


    if (ImgFound == ImgSource.length*(BoxesSolved+1)) {
      if (BoxesSolved == Max_boxes-1) {
        $("#transitionMessage").text("You completed all the boxes and finished this round before timer ran out! Congratulations!");
        $("#transitionMessage").show();
      }
      else {
        BoxesSolved++;
        resetGame(); 
      }
    }
    else {
    }
  }
}



$(function() {
  // Generate the card grid
for (var y = 1; y < 3 ; y++) {
	$.each(ImgSource1, function(i, val) {
		$(Source).append("<div id=card" + y + i + "><img src=" + val + " />");
	});
}
	$(Source + " div").click(OpenCard);
	ShuffleImages();
});