the_str = "[[254 252 248 251 248 243 231 212 188 173 163 159 163 169 162 154] [255 253 251 243 227 193 158 145 159 159 154 150 153 158 159 159] [246 228 211 170 179 156 70 50 73 138 193 197 165 144 152 173] [228 218 186 149 133 130 100 48 47 61 137 192 175 168 170 169] [212 200 170 147 121 85 124 65 69 137 185 240 221 174 171 193] [222 235 228 192 162 132 150 187 218 217 200 225 228 211 214 214] [187 230 244 231 213 236 232 220 222 218 216 213 204 199 207 195] [166 173 204 230 245 247 226 193 191 225 218 209 181 132 198 202] [189 171 210 210 210 179 210 211 203 192 213 188 106 151 204 184] [205 174 219 223 219 99 121 233 231 214 214 212 195 193 151 158] [209 137 166 212 204 115 117 202 222 219 210 204 168 114 84 204] [214 174 143 155 222 137 139 182 214 193 143 157 58 78 135 198] [227 230 222 191 173 129 148 150 184 140 103 147 125 144 165 204] [241 239 238 231 216 143 143 163 203 193 175 145 143 164 198 201] [250 248 250 245 243 219 135 94 134 156 160 179 194 198 198 198] [253 251 249 249 249 246 232 223 229 232 216 213 213 203 198 197]]"
new_str = ""
for i in range(len(the_str)):
    if the_str[i] == " ":
        new_str += ','
    else:
        new_str += the_str[i]

print(new_str)