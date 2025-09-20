# ---------- Build stage ----------
FROM eclipse-temurin:17-jdk as build
WORKDIR /app
COPY . .
RUN ./gradlew bootJar --no-daemon

# ---------- Run stage ----------
FROM eclipse-temurin:17-jre as run
WORKDIR /app
COPY --from=build /app/build/libs/*.jar app.jar
EXPOSE 8081
ENTRYPOINT ["java","-jar","app.jar"]
