# Phát hiện Bạo lực và Phát ngôn Thù ghét trong Video Theo Thời gian Thực

## Giới thiệu

Tài liệu này đề xuất một hệ thống để phát hiện nội dung bạo lực và phát ngôn thù ghét trong video dành cho trẻ em. Hệ thống sử dụng ba mô hình chính:

1. **Assembly AI** - Phát hiện phát ngôn thù ghét.
2. **MobileNetV2** - Phát hiện hình ảnh máu.
3. **Hybrid CNN-LSTM-Conv3D** - Phát hiện hành động bạo lực.

Các thí nghiệm được thực hiện trên 50 video ngắn từ YouTube, đạt độ chính xác 90% và độ nhạy 85%.

## Các điểm chính

### Bối cảnh và Nhu cầu

Trẻ em ngày càng tiếp xúc với mạng xã hội từ khi còn nhỏ, điều này gây lo ngại về sự phát triển nhận thức và tâm lý của chúng. Video chứa nội dung bạo lực hoặc phát ngôn thù ghét có thể gây ảnh hưởng tiêu cực.

### Mục tiêu Nghiên cứu

Phát triển một hệ thống theo dõi video theo thời gian thực để phát hiện và ngăn chặn nội dung không phù hợp với trẻ em.

### Phương pháp Tiếp cận

Hệ thống sử dụng các mô hình học sâu để phát hiện các dấu hiệu bạo lực và thù ghét trong video. Các mô hình này được tích hợp với Apache Spark và Kafka để xử lý video theo thời gian thực.

### Thử nghiệm và Kết quả

Thí nghiệm cho thấy hệ thống có khả năng phát hiện nội dung không phù hợp với độ chính xác cao và tốc độ xử lý đạt trung bình 40 khung hình mỗi giây.

### Kết luận

Hệ thống được đề xuất cung cấp một giải pháp hiệu quả cho vấn đề kiểm duyệt nội dung video trên mạng xã hội, đặc biệt là bảo vệ trẻ em khỏi các nội dung có hại.
