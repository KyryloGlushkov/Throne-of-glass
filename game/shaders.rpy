init python:
    import time

    def glass_time():
        return time.time()

    renpy.register_shader(
        "glass_text_shader",

        variables="""
            uniform float u_time;
            uniform sampler2D u_glass;
        """,

        vertex_200="""
            v_tex_coord = a_tex_coord;
        """,

        fragment_200="""
            vec4 text = texture2D(tex0, v_tex_coord);

        
            if (text.a < 0.01) discard;

            
            vec2 glass_uv = v_tex_coord;
            glass_uv.x += sin(u_time * 0.8) * 0.015;
            glass_uv.y += cos(u_time * 0.6) * 0.015;

            vec4 glass = texture2D(u_glass, glass_uv);

           
            vec3 color = mix(text.rgb, glass.rgb, 0.55);

            
            float shine = sin((v_tex_coord.x + u_time) * 12.0) * 0.08;
            color += shine;

            gl_FragColor = vec4(color, text.a);
        """
    )
