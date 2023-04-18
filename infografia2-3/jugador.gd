extends KinematicBody2D

const ACCEL = 500
const MAX_SPEED = 140
const FRICTION = 500
const MID_SPEED = 40

var velocity = Vector2.ZERO
onready var state_machine = $AnimationTree.get("parameters/playback")
var health = 10

func _input(event):
	if Input.is_action_just_pressed("damage"):
		health -= 1
		print("health: ", health)

func _physics_process(delta):
	# entrada de movimiento
	var input_vector = Vector2.ZERO # ( 0 , 0 )
	input_vector.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left") #(La velocidad en X es la diferencia entre la precionana de la tecla derecha e izquierda)
	input_vector.y = Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	input_vector = input_vector.normalized()
	#print(input_vector)
	
	if input_vector != Vector2.ZERO:
		# jugador en caminando
		velocity = velocity.move_toward(input_vector * MID_SPEED, ACCEL * delta)
		state_machine.travel("walk")
		if Input.is_action_pressed("run"):
			velocity = velocity.move_toward(input_vector * MAX_SPEED, ACCEL * delta)
			state_machine.travel("run")
		elif Input.is_action_just_released("run"):
			velocity = velocity.move_toward(input_vector * MID_SPEED, ACCEL * delta)
			state_machine.travel("walk")
		
	else:
		velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)
		state_machine.travel("iddle")
	
	# saltar
	if Input.is_action_pressed("jump"):
		state_machine.travel("jump")
		if Input.is_action_pressed("attack"):
			print("saltar y atacar")
			state_machine.travel("jumpattack")
	
	# atacar
	if Input.is_action_just_pressed("attack"): #Mapa de entrada
		state_machine.travel("attack") #animatio tree
		print("atacar")
		
	
	
	# morir
	if health <= 0:
		state_machine.travel("dead")
		velocity = Vector2.ZERO
	
	if velocity.x < 0:
		$Sprite.scale.x = -0.284
		$Sprite.scale.y = 0.298
	elif velocity.x > 0:
		$Sprite.scale.x = 0.284
		$Sprite.scale.y = 0.298
		
	#ejecutar movimiento
	velocity = move_and_slide(velocity)
