extends Control


# Called when the node enters the scene tree for the first time.
func _ready():
	$VBoxContainer/FishingButton.grab_focus()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta: float) -> void:
	pass

func _on_fishing_button_pressed():
	get_tree().change_scene_to_file("res://fishing.tscn")
func _on_quit_button_pressed():
	get_tree().change_scene_to_file("res://title_screen.tscn")
