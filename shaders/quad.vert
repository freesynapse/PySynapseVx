#version 330 core

layout(location=0) in vec3 a_position;
layout(location=1) in vec3 a_color;

out vec3 v_color;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

//
void main()
{
    v_color = a_color;
    gl_Position = m_proj * m_view * m_model * vec4(a_position, 1.0);
}