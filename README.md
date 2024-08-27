Tài liệu này đề xuất một hệ thống để phát hiện nội dung bạo lực và phát ngôn thù ghét trong video dành cho trẻ em. Hệ thống này sử dụng ba mô hình: Assembly AI (phát hiện phát ngôn thù ghét), MobileNetV2 (phát hiện máu), và mô hình kết hợp Hybrid CNN-LSTM-Conv3D (phát hiện hành động bạo lực). Các thí nghiệm được thực hiện trên 50 video ngắn từ YouTube với độ chính xác đạt 90% và độ nhạy đạt 85%.

Các điểm chính:

Bối cảnh và nhu cầu: Trẻ em ngày càng tiếp xúc với mạng xã hội từ khi còn nhỏ, điều này gây lo ngại về sự phát triển nhận thức và tâm lý của chúng. Video chứa nội dung bạo lực hoặc phát ngôn thù ghét có thể gây ảnh hưởng tiêu cực.

Mục tiêu nghiên cứu: Phát triển một hệ thống theo dõi video theo thời gian thực để phát hiện và ngăn chặn nội dung không phù hợp với trẻ em.

Phương pháp tiếp cận: Hệ thống sử dụng các mô hình học sâu để phát hiện các dấu hiệu bạo lực và thù ghét trong video. Các mô hình này được tích hợp với Apache Spark và Kafka để xử lý video theo thời gian thực.

Thử nghiệm và kết quả: Thí nghiệm cho thấy hệ thống có khả năng phát hiện nội dung không phù hợp với độ chính xác cao và tốc độ xử lý đạt trung bình 40 khung hình mỗi giây.

Kết luận: Hệ thống được đề xuất cung cấp một giải pháp hiệu quả cho vấn đề kiểm duyệt nội dung video trên mạng xã hội, đặc biệt là bảo vệ trẻ em khỏi các nội dung có hại.
