import bpy

def create_wall(length, width, height, location):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    wall = bpy.context.active_object
    wall.dimensions = (length, width, height)
    wall.name = "Wall"
    return wall

def create_door(width, height, location):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    door = bpy.context.active_object
    door.dimensions = (width, 0.1, height)
    door.name = "Door"
    return door

def create_ground(length, width, height):
    bpy.ops.mesh.primitive_plane_add(size=1, align='WORLD', location=(0, 0, height))
    ground = bpy.context.active_object
    ground.dimensions = (length, width, 1)
    ground.name = "Ground"
    return ground

def main():
    # Clear existing mesh objects in the scene
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Set parameters
    building_length = 20
    building_width = 20
    building_height = 3
    door_width = 5
    door_height = 2

    # Create a ground plane for the first floor
    create_ground(building_length, building_width, 0)

    # Create walls for the first floor
    front_wall1 = create_wall(building_length, 0.1, building_height, (0, building_width/2, building_height/2))
    back_wall1 = create_wall(building_length, 0.1, building_height, (0, -building_width/2, building_height/2))
    left_wall1 = create_wall(0.1, building_width, building_height, (-building_length/2, 0, building_height/2))
    right_wall1 = create_wall(0.1, building_width, building_height, (building_length/2, 0, building_height/2))

    # Create doors on opposite corners for the first floor
    create_door(door_width, door_height, (front_wall1.location.x - front_wall1.dimensions.x/2, front_wall1.location.y, door_height/2))
    create_door(door_width, door_height, (back_wall1.location.x + back_wall1.dimensions.x/2, back_wall1.location.y, door_height/2))

    # Create a ground plane for the second floor
    create_ground(building_length, building_width, building_height*2)

    # Create walls for the second floor
    front_wall2 = create_wall(building_length, 0.1, building_height, (0, building_width/2, building_height*2 + building_height/2))
    back_wall2 = create_wall(building_length, 0.1, building_height, (0, -building_width/2, building_height*2 + building_height/2))
    left_wall2 = create_wall(0.1, building_width, building_height, (-building_length/2, 0, building_height*2 + building_height/2))
    right_wall2 = create_wall(0.1, building_width, building_height, (building_length/2, 0, building_height*2 + building_height/2))

    # Create doors on opposite corners for the second floor
    create_door(door_width, door_height, (front_wall2.location.x - front_wall2.dimensions.x/2, front_wall2.location.y, building_height*2 + door_height/2))
    create_door(door_width, door_height, (back_wall2.location.x + back_wall2.dimensions.x/2, back_wall2.location.y, building_height*2 + door_height/2))

if __name__ == "__main__":
    main()
