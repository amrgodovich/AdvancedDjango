import csv, os
from movie.models import Movie, Rating, Tag, User, Link

def run():
    base_path = "Moviedb"
    print("📥 Import started...")

    # 1️⃣ Create 650 users
    users_to_create = [User(userId=uid, username="") for uid in range(1, 651)]
    User.objects.bulk_create(users_to_create, ignore_conflicts=True)
    print("✅ Created 650 users")

    # 2️⃣ Check required CSVs
    files = ["movies.csv", "links.csv", "ratings.csv", "tags.csv"]
    for file in files:
        full = os.path.join(base_path, file)
        if not os.path.exists(full):
            print(f"⚠️ Missing file: {full}")
            return

    # 3️⃣ Import Movies
    print("➡️ Importing movies...")
    with open(os.path.join(base_path, "movies.csv"), encoding="utf-8") as f:
        reader = csv.DictReader(f)
        movies = [
            Movie(
                movieId=int(r["movieId"]),
                title=r["title"],
                genres=r["genres"]
            )
            for r in reader
        ]
    Movie.objects.bulk_create(movies, ignore_conflicts=True)
    print(f"✅ Imported {len(movies)} movies")

    links = []
    with open(os.path.join(base_path, "links.csv"), encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                movie = Movie.objects.get(movieId=int(r["movieId"]))
                links.append(Link(
                    movieId=movie,  # pass the instance
                    imdbId=int(r["imdbId"]) if r["imdbId"] else None,
                    tmdbId=int(r["tmdbId"]) if r["tmdbId"] else None
                ))
            except Movie.DoesNotExist:
                continue  # skip if movie not found
    Link.objects.bulk_create(links, ignore_conflicts=True)



    # 5️⃣ Import Ratings
    print("➡️ Importing ratings...")
    with open(os.path.join(base_path, "ratings.csv"), encoding="utf-8") as f:
        reader = csv.DictReader(f)
        ratings = [
            Rating(
                userId_id=int(r["userId"]),
                movieId_id=int(r["movieId"]),
                rating=float(r["rating"]),
                timestamp=int(r["timestamp"])
            )
            for r in reader
        ]
    Rating.objects.bulk_create(ratings, ignore_conflicts=True)
    print(f"✅ Imported {len(ratings)} ratings")

    # 6️⃣ Import Tags
    print("➡️ Importing tags...")
    with open(os.path.join(base_path, "tags.csv"), encoding="utf-8") as f:
        reader = csv.DictReader(f)
        tags = [
            Tag(
                userId_id=int(r["userId"]),
                movieId_id=int(r["movieId"]),
                tag=r["tag"],
                timestamp=r["timestamp"]
            )
            for r in reader
        ]
    Tag.objects.bulk_create(tags, ignore_conflicts=True)
    print(f"✅ Imported {len(tags)} tags")

    print("🎉 All CSV data imported successfully!")
